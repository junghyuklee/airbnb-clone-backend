from django.conf import settings
from enum import Enum
import strawberry
from strawberry.types import Info
from strawberry import auto
import typing
from . import models
from wishlists.models import Wishlist
from users.types import UserType
from reviews.types import ReviewType


@strawberry.django.type(models.Room)
class RoomType:
    id: auto
    name: auto
    owner: UserType
    kind: auto
    country: auto
    city: auto
    price: auto

    @strawberry.field
    def reviews(self, page: typing.Optional[int] = 1) -> typing.List[ReviewType]:
        page_size = settings.PAGE_SIZE
        page_start = (page - 1) * page_size
        page_end = page_start + page_size
        return self.reviews.all().order_by("created_at")[page_start:page_end]

    @strawberry.field
    def rating(self) -> str:
        return self.rating()

    @strawberry.field
    def is_owner(self, info: Info) -> bool:
        return self.owner == info.context.request.user

    @strawberry.field
    def is_like(self, info: Info) -> bool:
        return Wishlist.objects.filter(
            user=info.context.request.user,
            rooms__id=self.id,
        ).exists()


@strawberry.enum
class RoomKindChoioces(Enum):
    ENTIRE_PLACE = "entire_place"
    PRIVATE_ROOM = "private_room"
    SHARED_ROOM = "shared_room"


@strawberry.input
class AddRoomType:
    name: str
    country: str
    city: str
    price: int
    rooms: int
    toilets: int
    description: str
    address: str
    pet_friendly: bool
    kind: RoomKindChoioces
    amenities: typing.List[int]
    category: int
