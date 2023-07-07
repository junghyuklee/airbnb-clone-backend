from rest_framework import serializers
from users.models import User
from rooms.models import Room
from experiences.models import Experience


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
