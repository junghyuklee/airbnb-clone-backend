from rest_framework.test import APITestCase
from . import models


class TestAmenity(APITestCase):
    NAME = "Amenity Detail Test"
    DESC = "Amenity Detail Test Desc"
    UPDATE_NAME = "Update Amenity"
    UPDATE_DESC = "Update Amenity Desc"

    URL = "/api/v1/rooms/amenities"

    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_amenity_not_found(self):
        response = self.client.get(f"{self.URL}/2")

        self.assertEqual(
            response.status_code,
            404,
            "Not 404 status code",
        )

    def test_get_amenity(self):
        response = self.client.get(f"{self.URL}/1")

        self.assertEqual(
            response.status_code,
            200,
            "Not 200 status code",
        )

        data = response.json()

        self.assertEqual(
            data["name"],
            self.NAME,
        )
        self.assertEqual(
            data["description"],
            self.DESC,
        )

    def test_put_amenity_max_len_err(self):
        response = self.client.put(
            f"{self.URL}/1",
            data={
                "name": "test" * 100,
                "description": "test" * 1000,
            },
        )
        data = response.json()
        self.assertEqual(
            response.status_code,
            400,
            "Not 400 status code",
        )
        self.assertIn("name", data)
        self.assertIn("description", data)

    def test_put_amenity(self):
        response = self.client.put(
            f"{self.URL}/1",
            data={
                "name": self.UPDATE_NAME,
                "description": self.UPDATE_DESC,
            },
        )
        data = response.json()
        self.assertEqual(
            response.status_code,
            200,
            "Not 200 status code",
        )
        self.assertEqual(
            data["name"],
            self.UPDATE_NAME,
        )
        self.assertEqual(
            data["description"],
            self.UPDATE_DESC,
        )

    def test_delete_amenity(self):
        response = self.client.delete(f"{self.URL}/1")

        self.assertEqual(
            response.status_code,
            204,
            "Not 204 status code",
        )
