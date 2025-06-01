from django.test import TestCase
from django.urls import reverse



DISH_URL = reverse("kitchen_board:dish_list")


class PublicDishTest(TestCase):
    def test_login_required(self) -> None:
        """Test that login is required for views."""
        response = self.client.get(DISH_URL)
        self.assertNotEqual(response.status_code, 200)

