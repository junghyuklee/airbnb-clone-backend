from rest_framework import serializers
from users.models import User
from rooms.models import Room
from experiences.models import Experience
from medias.serializers import PhotoSerializer


class TinyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "avatar",
            "username",
        )


class TinyRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = (
            "name",
            "rating",
            "photos",
        )


class TinyExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = (
            "name",
            "rating",
            "photos",
        )


class BookingRoomSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(read_only=True, many=True)

    class Meta:
        model = Room
        fields = (
            "name",
            "country",
            "city",
            "rating",
            "photos",
        )
