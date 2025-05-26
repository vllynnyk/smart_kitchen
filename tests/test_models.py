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
