from django.db import transaction
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    ParseError,
    PermissionDenied,
)
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Perk, Experience
from categories.models import Category
from .serializers import (
    PerkSerializer,
    ExperienceListSerializer,
    ExperienceDetailSerializer,
)


class Experiences(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_experiences = Experience.objects.all()
        serializer = ExperienceListSerializer(
            all_experiences,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = ExperienceDetailSerializer(data=request.data)
        if serializer.is_valid():
            category_pk = request.data.get("category")
            if not category_pk:
                raise ParseError("Category is required")
            try:
                category = Category.objects.get(pk=category_pk)
                if category.kind == Category.CategoryKindChoices.ROOMS:
                    raise ParseError("The category kind should be 'experiences'")
            except Category.DoesNotExist:
                raise ParseError("Category not found")
            try:
                with transaction.atomic():
                    experience = serializer.save(
                        host=request.user,
                        category=category,
                    )
                    perks = request.data.get("perks")
                    for perk_pk in perks:
                        perk = Perk.objects.get(pk=perk_pk)
                        experience.perks.add(perk)
                    serializer = ExperienceDetailSerializer(
                        experience,
                        context={"request": request},
                    )
                    return Response(serializer.data)
            except Exception:
                raise ParseError("Perk not found")
        else:
            return Response(serializer.errors)


class ExperienceDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Experience.objects.get(pk=pk)
        except Experience.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        experience = self.get_object(pk)
        serializer = ExperienceDetailSerializer(
            experience,
            context={"request": request},
        )
        return Response(serializer.data)

    def put(self, request, pk):
        experience = self.get_object(pk)
        if experience.host != request.user:
            raise PermissionDenied

        serializer = ExperienceDetailSerializer(
            experience,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            category_pk = request.data.get("category")
            if category_pk != None:
                try:
                    category = Category.objects.get(pk=category_pk)
                    if category.kind == Category.CategoryKindChoices.ROOMS:
                        raise ParseError("The category kind should be 'experiences'")
                except Category.DoesNotExist:
                    raise ParseError("Category not found")
            try:
                with transaction.atomic():
                    if category_pk == None:
                        update_experience = serializer.save(
                            owner=request.user,
                        )
                    else:
                        update_experience = serializer.save(
                            owner=request.user,
                            category=category,
                        )

                    perks = request.data.get("perks")
                    if perks != None:
                        update_experience.perks.clear()
                        for perk_pk in perks:
                            perk = Perks.objects.get(pk=perk_pk)
                            update_experience.perks.add(perk)

                    serializer = ExperienceDetailSerializer(
                        update_experience,
                        context={"request": request},
                    )
                    return Response(serializer.data)
            except Exception:
                raise ParseError("Perk not found")
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        experience = self.get_object(pk)
        if experience.host != request.user:
            raise PermissionDenied
        experience.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Perks(APIView):
    def get(self, request):
        all_perks = Perk.objects.all()
        serializer = PerkSerializer(all_perks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serialzer = PerkSerializer(data=request.data)
        if serialzer.is_valid():
            perk = serialzer.save()
            return Response(PerkSerializer(perk).data)
        else:
            return Response(serialzer.errors)


class PerkDetail(APIView):
    def get_object(self, pk):
        try:
            return Perk.objects.get(pk=pk)
        except Perk.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        perk = self.get_object(pk)
        serializer = PerkSerializer(perk)
        return Response(
            serializer.data,
        )

    def put(self, request, pk):
        perk = self.get_object(pk)
        serializer = PerkSerializer(
            perk,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            update_perk = serializer.save()
            return Response(
                PerkSerializer(update_perk).data,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        perk = self.get_object(pk)
        perk.delete()
        return Response(status=HTTP_204_NO_CONTENT)
