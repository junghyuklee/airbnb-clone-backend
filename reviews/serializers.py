from rest_framework import serializers
from .models import Review
from common.serializers import (
    TinyUserSerializer,
    TinyRoomSerializer,
    TinyExperienceSerializer,
)


class ReviewSerializer(serializers.ModelSerializer):
    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = (
            "user",
            "payload",
            "rating",
        )


class UserReviewSerializer(serializers.ModelSerializer):
    room = TinyRoomSerializer(read_only=True)
    experience = TinyExperienceSerializer(read_only=True)
    review_kind = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = (
            "room",
            "experience",
            "review_kind",
            "payload",
            "rating",
        )

    def get_review_kind(self, review):
        if review.room:
            return "ROOM"
        else:
            return "EXPERIENCE"
