from django.test import TestCase
from django.urls import reverse


DISH_TYPES_URL = reverse("kitchen_board:dish_type_list")

class PublicDishTypeTest(TestCase):
    def test_login_required(self):
        """Test that login is required for views."""
        response = self.client.get(DISH_TYPES_URL)
        self.assertNotEqual(response.status_code, 200)
