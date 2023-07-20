from rest_framework.test import APITestCase
from . import models
from users.models import User


class TestRooms(APITestCase):
    URL = "/api/v1/rooms/"

    def setUp(self):
        user = User.objects.create(
            username="test",
        )
        user.set_password("123")
        user.save()
        self.user = user

    def test_create_room_no_auth(self):
        self.client.logout()

        response = self.client.post(f"{self.URL}")
        self.assertEqual(response.status_code, 403)

    def test_create_room(self):
        self.client.force_login(self.user)

        response = self.client.post(f"{self.URL}")
        print(response.json())
