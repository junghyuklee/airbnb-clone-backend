from django.urls import path
from . import views

urlpatterns = [
    path("", views.Experiences.as_view()),
    path("<int:pk>", views.ExperienceDetail.as_view()),
    # path("<int:pk>/reviews", views.RoomReviews.as_view()),
    # path("<int:pk>/photos", views.RoomPhotos.as_view()),
    # path("<int:pk>/bookings", views.RoomBookings.as_view()),
    path("perks/", views.Perks.as_view()),
    path("perks/<int:pk>", views.PerkDetail.as_view()),
]
