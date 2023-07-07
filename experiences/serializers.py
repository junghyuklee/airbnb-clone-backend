from rest_framework import serializers
from .models import Perk, Experience
from wishlists.models import Wishlist
from common.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from medias.serializers import PhotoSerializer, VideoSerializer


class PerkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perk
        fields = (
            "name",
            "details",
            "explanation",
        )


class ExperienceListSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    is_host = serializers.SerializerMethodField()
    video = VideoSerializer(read_only=True)

    class Meta:
        model = Experience
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "is_host",
            "video",
        )

    def get_rating(self, experience):
        return experience.rating()

    def get_is_host(self, experience):
        request = self.context["request"]
        return experience.host == request.user


class ExperienceDetailSerializer(serializers.ModelSerializer):
    host = TinyUserSerializer(read_only=True)
    perks = PerkSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.SerializerMethodField()
    is_host = serializers.SerializerMethodField()
    is_like = serializers.SerializerMethodField()
    photos = PhotoSerializer(read_only=True, many=True)
    video = VideoSerializer(read_only=True)

    class Meta:
        model = Experience
        fields = "__all__"

    def get_rating(self, experience):
        return experience.rating()

    def get_is_host(self, experience):
        request = self.context["request"]
        return experience.host == request.user

    def get_is_like(self, experience):
        request = self.context["request"]
        return Wishlist.objects.filter(
            user=request.user,
            experiences__pk=experience.pk,
        ).exists()
