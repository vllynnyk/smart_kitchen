from django.urls import path

from kitchen_board.views import (
    index,
    DishTypeListView,
    DishTypeDetailView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    IngredientListView,
    IngredientDetailView,
    IngredientCreateView,
    IngredientUpdateView,
    IngredientDeleteView,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookPositionUpdateView,
    CookDeleteView
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
        "dish_types/<int:pk>/",
         DishTypeDetailView.as_view(),
         name="dish_type_detail"
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
    path(
        "ingredients/<int:pk>/",
        IngredientDetailView.as_view(),
        name="ingredient_detail"
    ),
    path(
        "ingredients/create/",
        IngredientCreateView.as_view(),
        name="ingredient_create"
    ),
    path(
        "ingredients/<int:pk>/update/",
        IngredientUpdateView.as_view(),
        name="ingredient_update"
    ),
    path(
        "ingredients/<int:pk>/delete/",
        IngredientDeleteView.as_view(),
        name="ingredient_delete"
    ),
#Dish URLs
    path("dishes/",
         DishListView.as_view(),
         name="dish_list"
         ),
    path(
        "dishes/<int:pk>/",
        DishDetailView.as_view(),
        name="dish_detail"
    ),
    path(
        "dishes/create/",
         DishCreateView.as_view(),
         name="dish_create"),
    path(
        "dishes/<int:pk>/update/",
         DishUpdateView.as_view(),
         name="dish_update"
    ),
    path(
        "dishes/<int:pk>/delete/",
         DishDeleteView.as_view(),
         name="dish_delete"
    ),
#Cook URLs
    path(
        "cooks/",
        CookListView.as_view(),
        name="cook_list"
    ),
    path(
        "cooks/<int:pk>/",
        CookDetailView.as_view(),
        name="cook_detail"
    ),
    path(
        "cooks/create/",
        CookCreateView.as_view(),
        name="cook_create"
    ),
    path(
        "cooks/<int:pk>/update/",
        CookPositionUpdateView.as_view(),
        name="cook_update"
    ),
    path(
        "cooks/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook_delete"
    ),
]
