from django.test import TestCase

from kitchen_board.models import DishType


class DishTypeTest(TestCase):

    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="Soups")
        self.assertEqual(str(dish_type), dish_type.name)
