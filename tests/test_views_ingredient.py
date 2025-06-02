from django.test import TestCase
from django.urls import reverse


INGREDIENT_URL = reverse("kitchen_board:ingredient_list")


class PublicIngredientTest(TestCase):
    def test_login_required(self) -> None:
        """Test that login is required for views."""
        response = self.client.get(INGREDIENT_URL)
        self.assertNotEqual(response.status_code, 200)

