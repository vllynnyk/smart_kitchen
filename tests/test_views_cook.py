from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen_board.models import Cook

COOK_URL = reverse("kitchen_board:cook_list")


class PublicCookTest(TestCase):
    def test_login_required(self) -> None:
        """Test that login is required for views."""
        response = self.client.get(COOK_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateCookTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="user1",
            password="1234pass",
        )
        Cook.objects.create(
            username="God",
            first_name="John",
            last_name="Smith",
            position="head_chef",
            years_of_experience=10
        )
        Cook.objects.create(
            username="Devil",
            first_name="Bob",
            last_name="Bobson",
            position="line_cook",
            years_of_experience=12
        )
        Cook.objects.create(
            username="Angel",
            first_name="Jack",
            last_name="Jackson",
            position="prep_cook",
            years_of_experience=3
        )

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_uses_correct_context(self):
        response = self.client.get(COOK_URL)
        self.assertTemplateUsed(response, "kitchen_board/cook_list.html")
        self.assertIn("search_form", response.context)
