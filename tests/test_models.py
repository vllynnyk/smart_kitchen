from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from kitchen_board.models import DishType, Cook, Ingredient, Dish


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

    def test_position_choice(self):
        cook = get_user_model()(
            username="john_d",
            password="1234pass",
            position="dishwasher"
        )
        with self.assertRaises(ValidationError):
            cook.full_clean()

    def test_cook_ordering_by_username(self):
        get_user_model().objects.create_user(
            username="john_w",
            password="1234pass",
        )
        get_user_model().objects.create_user(
            username="john_d",
            password="1234pass",
        )
        all_cook = Cook.objects.all()
        self.assertEqual(all_cook[0].username, "john_d")


class IngredientTest(TestCase):
    def test_ingredient_str(self):
        ingredient = Ingredient.objects.create(
            name="Apple",
            stock_count=10,
        )
        self.assertEqual(str(ingredient),
                         f"{ingredient.name} ({ingredient.stock_count})")

    def test_ingredient_ordering(self):
            Ingredient.objects.create(
                name="Banana",
                stock_count=5,
            )
            Ingredient.objects.create(
                name="Apple",
                stock_count=10,
            )
            all_ingredients = Ingredient.objects.all()
            self.assertEqual(all_ingredients[0].name, "Apple")


class DishTest(TestCase):
    def test_dish_str(self):
        dish_type = DishType.objects.create(name="Dessert")
        dish = Dish.objects.create(
            name="Apple Pie",
            description="Delicious apple pie",
            price=10.20,
            dish_type=dish_type,
        )
        self.assertEqual(str(dish),
                         f"{dish.name}"
                         f" {dish.price}"
                         f" {dish.dish_type.name}")
