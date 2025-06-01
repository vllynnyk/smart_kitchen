from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen_board.models import Dish

DISH_URL = reverse("kitchen_board:dish_list")


class PublicDishTest(TestCase):
    def test_login_required(self) -> None:
        """Test that login is required for views."""
        response = self.client.get(DISH_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateDishTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="user1",
            password="1234pass",
        )
        Dish.objects.create(name="Margarita")
        Dish.objects.create(name="Curry")
        Dish.objects.create(name="Sushi")

    def setUp(self) -> None:
        self.client.force_login(self.user)
