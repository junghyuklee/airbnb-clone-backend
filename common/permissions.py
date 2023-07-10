from strawberry.types import Info
from strawberry.permission import BasePermission
import typing


class OnlyLoggedIn(BasePermission):
    message = "You need to be logged in for this"

    def has_permission(self, source: typing.Any, info: Info, **kwargs):
        return info.context.request.user.is_authenticated
