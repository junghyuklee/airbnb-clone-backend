from rest_framework import serializers
from .models import User
from reviews.models import Review
from reviews.serializers import UserReviewSerializer


class PrivateUserSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "avatar",
            "name",
            "last_login",
            "date_joined",
            "reviews",
            "is_host",
            "rooms",
            "experiences",
            "gender",
            "language",
            "currency",
        )

    def get_reviews(self, user):
        reviews = Review.objects.filter(user=user).order_by("created_at")[0:3]
        serializer = UserReviewSerializer(reviews, many=True)
        return serializer.data


class signUpUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "name",
        )
