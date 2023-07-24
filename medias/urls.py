from django.urls import path
from .views import PhotoDetail, VideoDetail, GetUploadUrl

urlpatterns = [
    path("photos/get-url", GetUploadUrl.as_view()),
    path("photos/<int:pk>", PhotoDetail.as_view()),
    path("videos/<int:pk>", VideoDetail.as_view()),
]
