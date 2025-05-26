from django.urls import path

from kitchen_board.views import index


app_name = "kitchen_board"

urlpatterns = [
    path("", index, name="index"),
]
