from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView

from kitchen_board.forms import DishForm, CookCreationForm, CookPositionUpdateForm
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


#DishType
class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "kitchen_board/dish_type_list.html"
    paginate_by = 10


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    context_object_name = "dish_type"
    success_url = reverse_lazy("kitchen_board:dish_type_list")
    template_name = "kitchen_board/dish_type_form.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    context_object_name = "dish_type"
    success_url = reverse_lazy("kitchen_board:dish_type_list")
    template_name = "kitchen_board/dish_type_form.html"


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    context_object_name = "dish_type"
    success_url = reverse_lazy("kitchen_board:dish_type_list")
    template_name = "kitchen_board/dish_type_confirm_delete.html"


#Ingredient
class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    paginate_by = 10


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen_board:ingredient_list")


class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen_board:ingredient_list")


class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("kitchen_board:ingredient_list")


#Dish
class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 10
    queryset = Dish.objects.select_related("dish_type")


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen_board:dish_list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen_board:dish_list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen_board:dish_list")


#Cook
class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 10


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("kitchen_board:cook_list")


class CookPositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookPositionUpdateForm
    success_url = reverse_lazy(
        "kitchen_board:cook_list"
    )
