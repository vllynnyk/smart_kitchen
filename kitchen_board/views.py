from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from kitchen_board.models import Cook, DishType, Dish, Ingredient


@login_required
def index(request):
    """View function for home page of the site."""

    num_cooks = Cook.objects.count()
    num_dish_types = DishType.objects.count()
    num_dishes = Dish.objects.count()
    num_ingredients = Ingredient.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_cooks": num_cooks,
        "num_dish_types": num_dish_types,
        "num_dish": num_dishes,
        "num_ingredients": num_ingredients,
        "num_visits": num_visits + 1,
    }

    return render(request, "kitchen_board/index.html", context=context)
