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
