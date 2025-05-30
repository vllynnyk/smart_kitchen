from django.contrib.auth.forms import UserCreationForm


from kitchen_board.models import Cook


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
