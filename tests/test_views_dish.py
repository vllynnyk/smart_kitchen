from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen_board.models import Dish, DishType, Ingredient

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
        dish_type = DishType.objects.create(name="Pizza")
        Dish.objects.create(
            name="Margarita",
            price=100,
            dish_type=dish_type,
        )
        Dish.objects.create(
            name="Curry",
            price=100,
            dish_type=dish_type,
        )
        Dish.objects.create(
            name="Sushi",
            price=100,
            dish_type=dish_type,
        )

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_uses_correct_context(self):
        response = self.client.get(DISH_URL)
        self.assertTemplateUsed(response, "kitchen_board/dish_list.html")
        self.assertIn("search_form", response.context)

    def test_list_dish_type(self):
        response = self.client.get(DISH_URL)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Margarita")
        self.assertContains(response, "Curry")
        self.assertContains(response, "Sushi")

    def test_list_dish_type_search_by_name(self):
        response = self.client.get(DISH_URL, {"name": "cu"})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Margarita")
        self.assertContains(response, "Curry")
        self.assertNotContains(response, "Sushi")

    def test_search_with_no_match(self):
        response = self.client.get(DISH_URL, {"name": "sen"})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Margarita")
        self.assertNotContains(response, "Curry")
        self.assertNotContains(response, "Sushi")
        self.assertContains(response,
                            "There are no dishes on the Kitchen Board.",
                            html=True)

    def test_create_dish(self):
        response = self.client.post(reverse("kitchen_board:dish_create"),{"name": "Meatballs"})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,DISH_URL)
        exists = Dish.objects.filter(name="Meatballs").exists()
        self.assertTrue(exists)

    def test_update_dish(self):
        dish = Dish.objects.get(name="Curry")
        response = self.client.post(reverse(
            "kitchen_board:dish_update",
            kwargs={"pk": dish.pk}
        ),
            {"name": "Meatballs"})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, DISH_URL)
        exists = Dish.objects.filter(name="Meatballs").exists()
        self.assertTrue(exists)

    def test_delete_dish(self):
        dish = Dish.objects.get(name="Sushi")
        response = self.client.post(
            reverse(
                "kitchen_board:dish_delete",
                kwargs={"pk": dish.pk}
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, DISH_URL)
        exists = Dish.objects.filter(name="Sushi").exists()
        self.assertFalse(exists)

    def test_detail_dish(self):
        dish = Dish.objects.get(name="Margarita")
        response = self.client.get(
            reverse(
                "kitchen_board:dish_detail",
                kwargs={"pk": dish.pk}
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,dish.name)
        self.assertTemplateUsed(response, "kitchen_board/dish_detail.html")
        self.assertEqual(response.context["dish"], dish)
