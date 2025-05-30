from django.urls import path

from kitchen_board.views import index, DishTypeListView


app_name = "kitchen_board"

urlpatterns = [
    path("", index, name="index"),
    #DishType URLs
    path(
        "dish_types/",
         DishTypeListView.as_view(),
         name="dish_type_list"
    ),
]
