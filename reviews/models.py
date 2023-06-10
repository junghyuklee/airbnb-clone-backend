from django.db import models
from common.models import CommonModel


class Review(CommonModel):
    """Review from a User to a Room or Experiences"""

    class RatingKindChoices(models.IntegerChoices):
        ONE_STAR = 1
        TWO_STAR = 2
        THREE_STAR = 3
        FOUR_STAR = 4
        FIVE_STAR = 5

    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_DEFAULT,
        default="deleted",
    )
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    payload = models.TextField()
    rating = models.PositiveIntegerField(
        choices=RatingKindChoices.choices,
    )

    def __str__(self) -> str:
        return f"{self.user} ({self.rating}⭐️)"
