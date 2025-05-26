from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen_board.models import DishType


class DishTypeTest(TestCase):

    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="Soups")
        self.assertEqual(str(dish_type), dish_type.name)

    def test_dish_type_ordering(self):
        """
        Test that DishType objects are ordered alphabetically by their 'name' field.
        """
        DishType.objects.create(name="Soups")
        DishType.objects.create(name="Pizza")
        all_dish_types = list(DishType.objects.all())
        self.assertEqual(all_dish_types[0]. name, "Pizza")


class CookTest(TestCase):

    def setUp(self):
        self.cook = get_user_model().objects.create_user(
            username="john_j",
            first_name="John",
            last_name="Jones",
            password="1234pass",
            position = "head_chef",
            years_of_experience=5,
        )

    def test_cook_str(self):
        cook = self.cook
        self.assertEqual(str(cook),
                         f"{cook.username}"
                         f" ({cook.first_name} {cook.last_name})")


    def test_cook_creation(self):
        self.assertEqual(self.cook.position, "head_chef")
        self.assertEqual(self.cook.years_of_experience, 5)
