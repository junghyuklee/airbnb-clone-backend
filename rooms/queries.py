from . import models


def get_all_rooms():
    return models.Room.objects.all()


def get_room(id: int):
    try:
        return models.Room.objects.get(id=id)
    except models.Room.DoesNotExist:
        return None
