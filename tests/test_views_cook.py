from django.test import TestCase
from django.urls import reverse


COOK_URL = reverse("kitchen_board:cook_list")


class PublicCookTest(TestCase):
    def test_login_required(self) -> None:
        """Test that login is required for views."""
        response = self.client.get(COOK_URL)
        self.assertNotEqual(response.status_code, 200)

