from django.contrib.auth import get_user_model
from django.forms import forms
from django.contrib.auth.forms import UserCreationForm

from kitchen_board.models import Cook, Ingredient, Dish


# Forms for model Cook
class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "position",
            "years_of_experience",
        )


class CookPositionUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = [
            "position",
            "years_of_experience",
        ]


# Form for model Dish
class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Dish
        fields = "__all__"
