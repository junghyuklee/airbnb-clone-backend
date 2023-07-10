from django.db import transaction
import strawberry
from strawberry.types import Info
from .types import AddRoomType
from .models import Amenity, Room
from categories.models import Category


def add_room(info: Info, add_room: AddRoomType):
    category_pk = add_room.category
    if not category_pk:
        raise ValueError("Categorty is required")
    try:
        category = Category.objects.get(pk=category_pk)
        if category.kind == Category.CategoryKindChoices.EXPERIENCES:
            raise ValueError("The category kind should be 'rooms'")
    except Category.DoesNotExist:
        raise ValueError("Category not found")
    try:
        with transaction.atomic():
            room = Room.objects.create(
                name=add_room.name,
                country=add_room.country,
                city=add_room.city,
                price=add_room.price,
                rooms=add_room.rooms,
                toilets=add_room.toilets,
                description=add_room.description,
                address=add_room.address,
                pet_friendly=add_room.pet_friendly,
                kind=add_room.kind,
                owner=info.context.request.user,
                category=category,
            )
            for amenity_pk in add_room.amenities:
                amenity = Amenity.objects.get(pk=amenity_pk)
                room.amenities.add(amenity)
            room.save()
            return room
    except Exception:
        raise ValueError("Amenity not found")
