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

    def test_search_with_no_match(self):
        response = self.client.get(DISH_TYPES_URL, {"name": "sen"})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Pizza")
        self.assertNotContains(response, "Soups")
        self.assertNotContains(response, "Salads")
        self.assertContains(response,
                            "There are no dish types on the Kitchen Board.",
                            html=True)

    def test_create_dish_type(self):
        response = self.client.post(
            reverse("kitchen_board:dish_type_create"),
            {"name": "Appetizers"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, DISH_TYPES_URL)
        exists = DishType.objects.filter(name="Appetizers").exists()
        self.assertTrue(exists)

    def test_update_dish_type(self):
        dish_type = DishType.objects.get(name="Pizza")
        response = self.client.post(reverse(
            "kitchen_board:dish_type_update",
            kwargs={"pk": dish_type.pk}
        ),
            {"name": "Starters"})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, DISH_TYPES_URL)
        exists = DishType.objects.filter(name="Starters").exists()
        self.assertTrue(exists)

    def test_delete_dish_type(self):
        dish_type = DishType.objects.get(name="Pizza")
        response = self.client.post(
            reverse(
                "kitchen_board:dish_type_delete",
                kwargs={"pk": dish_type.pk}
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, DISH_TYPES_URL)
        exists = DishType.objects.filter(name="Pizza").exists()
        self.assertFalse(exists)

    def test_detail_dish_type(self):
        dish_type = DishType.objects.get(name="Salads")
        response = self.client.get(
            reverse(
                "kitchen_board:dish_type_detail",
                kwargs={"pk": dish_type.pk}
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, dish_type.name)
        self.assertTemplateUsed(
            response,
            "kitchen_board/dish_type_detail.html"
        )
        self.assertEqual(response.context["dish_type"], dish_type)
