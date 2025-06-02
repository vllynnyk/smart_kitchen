from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen_board.models import Ingredient

INGREDIENT_URL = reverse("kitchen_board:ingredient_list")


class PublicIngredientTest(TestCase):
    def test_login_required(self) -> None:
        """Test that login is required for views."""
        response = self.client.get(INGREDIENT_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateIngredientTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="user1",
            password="1234pass",
        )
        Ingredient.objects.create(name="Apple")
        Ingredient.objects.create(name="Tomato")
        Ingredient.objects.create(name="Cheese")

    def setUp(self) -> None:
        self.client.force_login(self.user)
