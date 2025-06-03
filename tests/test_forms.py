from django.test import TestCase

from kitchen_board.forms import (
    CookCreationForm,
    CookPositionUpdateForm,
    DishForm,
    CookSearchForm,
    DishTypeSearchForm,
    IngredientSearchForm,
    DishSearchForm
)
from kitchen_board.models import Cook, Ingredient, DishType


class FormsTests(TestCase):
    def setUp(self):
        self.cook1 = Cook.objects.create(
            username="Angel",
            first_name="Jack",
            last_name="Smith",
            position="head_chef",
            years_of_experience=9
        )
        self.cook2 = Cook.objects.create(
            username="Angel",
            first_name="Bob",
            last_name="Smith",
            position="head_chef",
            years_of_experience=8
        )
        self.ingredient1 = Ingredient.objects.create(
            name="Cheese",
            stock_count=10
        )
        self.ingredient2 = Ingredient.objects.create(
            name="Tomato",
            stock_count=9
        )
        self.dish_type = DishType.objects.create(
            name="Pizza",
        )

    def test_cook_creation_form(self):
        form_data = {
            "username": "God",
            "password1": "1234pass",
            "password2": "1234pass",
            "first_name": "John",
            "last_name": "Johnson",
            "position": "pastry_chef",
            "years_of_experience": 10,
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"],
                         form_data["username"])
        self.assertEqual(form.cleaned_data["first_name"],
                         form_data["first_name"])
        self.assertEqual(form.cleaned_data["last_name"],
                         form_data["last_name"])
        self.assertEqual(
            form.cleaned_data["position"],
            form_data["position"]
        )
        self.assertEqual(
            form.cleaned_data["years_of_experience"],
            form_data["years_of_experience"]
        )

    def test_cook_updating_form(self):
            form_data = {
                "position": "pastry_chef",
                "years_of_experience": 10,
            }
            form = CookPositionUpdateForm(data=form_data, instance=self.cook1)
            self.assertTrue(form.is_valid())
            self.assertEqual(form.cleaned_data["position"], form_data["position"])
            self.assertEqual(form.cleaned_data["years_of_experience"], form_data["years_of_experience"])

    def test_dish_form(self):
        form_data = {
            "name": "Margarita",
            "description": "Delicious pizza",
            "price": 17.80,
            "dish_type": self.dish_type.id,
            "ingredients": [self.ingredient1.id, self.ingredient2.id],
            "cooks": [self.cook1.id, self.cook2.id],
        }
        form = DishForm(data=form_data)
        self.assertTrue(form.is_valid())
        dish = form.save()
        self.assertEqual(dish.name, form_data["name"])
        self.assertEqual(dish.dish_type, self.dish_type)
        self.assertCountEqual(
            list(dish.ingredients.all()),
            [self.ingredient1, self.ingredient2]
        )
        self.assertCountEqual(
            list(dish.cooks.all()),
            [self.cook1, self.cook2]
        )


class BaseSearchFormTest(TestCase):
    form_class = None
    field_name = None
    test_value = None

    def test_empty_form_is_valid(self):
        form = self.form_class(data={})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data[self.field_name], '')

    def test_form_with_value_is_valid(self):
        form = self.form_class(data={self.field_name: self.test_value})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data[self.field_name], self.test_value)

    def test_form_with_too_long_value_is_invalid(self):
        too_long_value = "a" * 101
        form = self.form_class(data={self.field_name: too_long_value})
        self.assertFalse(form.is_valid())
        self.assertIn(self.field_name, form.errors)


class CookSearchFormTest(BaseSearchFormTest):
    form_class = CookSearchForm
    field_name = "username"
    test_value = "Angel"


class DishTypeSearchFormTest(BaseSearchFormTest):
    form_class = DishTypeSearchForm
    field_name = "name"
    test_value = "Pizza"


class IngredientSearchFormTest(BaseSearchFormTest):
    form_class = IngredientSearchForm
    field_name = "name"
    test_value = "Apple"


class DishSearchFormTest(BaseSearchFormTest):
    form_class = DishSearchForm
    field_name = "name"
    test_value = "Margarita"
