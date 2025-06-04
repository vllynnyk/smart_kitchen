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
        Ingredient.objects.create(
            name="Apple",
            stock_count=10
        )
        Ingredient.objects.create(
            name="Tomato",
            stock_count=8
        )
        Ingredient.objects.create(
            name="Cheese",
            stock_count=6
        )

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_uses_correct_context(self):
        response = self.client.get(INGREDIENT_URL)
        self.assertTemplateUsed(response, "kitchen_board/ingredient_list.html")
        self.assertIn("search_form", response.context)

    def test_list_ingredient(self):
        response = self.client.get(INGREDIENT_URL)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Apple")
        self.assertContains(response, "Tomato")
        self.assertContains(response, "Cheese")

    def test_list_ingredient_search_by_name(self):
        response = self.client.get(INGREDIENT_URL, {"name": "pp"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Apple")
        self.assertNotContains(response, "Tomato")
        self.assertNotContains(response, "Cheese")

    def test_search_with_no_match(self):
        response = self.client.get(INGREDIENT_URL, {"name": "bi"})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Apple")
        self.assertNotContains(response, "Tomato")
        self.assertNotContains(response, "Cheese")
        self.assertContains(response,
                            "There are no ingredients on the Kitchen Board.",
                            html=True)

    def test_create_ingredient(self):
        response = self.client.post(
            reverse("kitchen_board:ingredient_create"),
            {
                "name": "Banana",
                "stock_count": 10
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,INGREDIENT_URL)
        exists = Ingredient.objects.filter(name="Banana").exists()
        self.assertTrue(exists)

    def test_update_ingredient(self):
        ingredient = Ingredient.objects.get(name="Cheese")
        response = self.client.post(reverse(
            "kitchen_board:ingredient_update",
            kwargs={"pk": ingredient.pk}
        ),
            {"name": "Banana", "stock_count": 12})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, INGREDIENT_URL)
        exists = Ingredient.objects.filter(name="Banana").exists()
        self.assertTrue(exists)

    def test_delete_ingredient(self):
        ingredient = Ingredient.objects.get(name="Cheese")
        response = self.client.post(
            reverse(
                "kitchen_board:ingredient_delete",
                kwargs={"pk": ingredient.pk}
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, INGREDIENT_URL)
        exists = Ingredient.objects.filter(name="Cheese").exists()
        self.assertFalse(exists)

    def test_detail_ingredient(self):
        ingredient = Ingredient.objects.get(name="Tomato")
        response = self.client.get(
            reverse(
                "kitchen_board:ingredient_detail",
                kwargs={"pk": ingredient.pk}
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,ingredient.name)
        self.assertTemplateUsed(
            response,
            "kitchen_board/ingredient_detail.html"
        )
        self.assertEqual(response.context["ingredient"], ingredient)
