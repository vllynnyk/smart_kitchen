from django.urls import path

from kitchen_board.views import (
    index,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    IngredientListView,
    DishListView,
    CookListView
)


app_name = "kitchen_board"

urlpatterns = [
    path("", index, name="index"),
    #DishType URLs
    path(
        "dish_types/",
         DishTypeListView.as_view(),
         name="dish_type_list"
    ),
    path(
        "dish_types/create/",
        DishTypeCreateView.as_view(),
        name="dish_type_create"
    ),
    path(
        "dish_types/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish_type_update"
    ),
    path(
        "dish_types/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish_type_delete"
    ),
    #Ingredient URLs
    path(
        "ingredients/",
        IngredientListView.as_view(),
        name="ingredient_list"
    ),
    #Dish URLs
    path("dishes/",
         DishListView.as_view(),
         name="dish_list"
         ),
    #Cook URLs
    path(
        "cooks/",
        CookListView.as_view(),
        name="cook_list"
    ),
]
