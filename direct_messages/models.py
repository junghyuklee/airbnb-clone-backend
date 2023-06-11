from django.db import models
from common.models import CommonModel


class ChattingRoom(CommonModel):
    users = models.ManyToManyField("users.User", related_name="chattingrooms")

    def __str__(self) -> str:
        return "Chatting Room."


class Message(CommonModel):
    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="messages",
    )
    room = models.ForeignKey(
        "direct_messages.ChattingRoom",
        on_delete=models.CASCADE,
        related_name="messages",
    )

    def __str__(self) -> str:
        return f"{self.user} says: {self.text}"
