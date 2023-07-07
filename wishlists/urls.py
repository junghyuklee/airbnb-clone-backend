from django.urls import path
from .views import (
    Wishlists,
    WishlistDetail,
    WishlistRoomToggle,
    WishlistExperienceToggle,
)

urlpatterns = [
    path("", Wishlists.as_view()),
    path("<int:pk>", WishlistDetail.as_view()),
    path("<int:pk>/rooms/<int:room_pk>", WishlistRoomToggle.as_view()),
    path(
        "<int:pk>/experiences/<int:experience_pk>", WishlistExperienceToggle.as_view()
    ),
]
