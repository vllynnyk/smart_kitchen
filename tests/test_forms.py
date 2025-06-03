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
