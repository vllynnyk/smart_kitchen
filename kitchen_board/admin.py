from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen_board.models import (Cook,
                                  DishType,
                                  Ingredient,
                                  Dish,)


admin.site.register(DishType)


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("position", "years_of_experience",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "position",
                    "years_of_experience",
                )
            },
        ),
    )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "dish_type")
    search_fields = ("name",)
    list_filter = ("dish_type",)
