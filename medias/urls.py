from django.urls import path
from .views import PhotoDetail

urlpatterns = [
    path("photos/<int:pt>", PhotoDetail.as_view()),
    path("videos/<int:pt>", PhotoDetail.as_view()),
]
