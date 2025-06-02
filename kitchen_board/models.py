from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from smart_kitchen import settings


class DishType(models.Model):
    name = models.CharField(max_length=65, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    POSITION_CHOICES = [
        ("head_chef", "Head Chef"),
        ("sous_chef", "Sous Chef"),
        ("pastry_chef", "Pastry Chef"),
        ("line_cook", "Line Cook"),
        ("grill_cook", "Grill Cook"),
        ("saucier", "Saucier"),
        ("garde_manger", "Garde Manger"),
        ("prep_cook", "Prep Cook"),
        ("commis", "Commis"),
    ]
    position = models.CharField(max_length=65, choices=POSITION_CHOICES)
    years_of_experience = models.PositiveIntegerField(default=0,)

    class Meta:
        verbose_name = "Cook"
        verbose_name_plural = "Cooks"
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def clean(self):
        super().clean()
        valid_position = [choice[0] for choice in self.POSITION_CHOICES]
        if self.position not in valid_position:
            raise ValidationError("Invalid position selected")

    def get_absolute_url(self):
        return reverse("kitchen_board:cook_detail", kwargs={"pk": self.pk})


class Ingredient(models.Model):
    name = models.CharField(max_length=65, unique=True)
    stock_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.stock_count})"


class Dish(models.Model):
    name = models.CharField(max_length=65, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    dish_type = models.ForeignKey(DishType,related_name="dishes" ,on_delete=models.CASCADE)
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="dishes")
    ingredients = models.ManyToManyField(Ingredient, related_name="dishes")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} {self.price} {self.dish_type.name}"
