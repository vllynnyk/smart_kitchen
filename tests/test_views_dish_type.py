from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen_board.models import DishType

DISH_TYPES_URL = reverse("kitchen_board:dish_type_list")


class PublicDishTypeTest(TestCase):
    def test_login_required(self) -> None:
        """Test that login is required for views."""
        response = self.client.get(DISH_TYPES_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateDishTypeTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="user1",
            password="1234pass",
        )
        DishType.objects.create(name="Pizza")
        DishType.objects.create(name="Soups")
        DishType.objects.create(name="Salads")

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_uses_correct_context(self):
        response = self.client.get(DISH_TYPES_URL)
        self.assertTemplateUsed(response, "kitchen_board/dish_type_list.html")
        self.assertIn("search_form", response.context)

    def test_list_dish_type(self):
        response = self.client.get(DISH_TYPES_URL)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pizza")
        self.assertContains(response, "Soups")
        self.assertContains(response, "Salads")

    def test_list_dish_type_search_by_name(self):
        response = self.client.get(DISH_TYPES_URL, {"name": "so"})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Pizza")
        self.assertContains(response, "Soups")
        self.assertNotContains(response, "Salads")
