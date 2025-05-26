from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


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
