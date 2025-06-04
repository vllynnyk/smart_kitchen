from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen_board.models import Cook

COOK_URL = reverse("kitchen_board:cook_list")


class PublicCookTest(TestCase):
    def test_login_required(self) -> None:
        """Test that login is required for views."""
        response = self.client.get(COOK_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateCookTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="user1",
            password="1234pass",
        )
        Cook.objects.create(
            username="God",
            first_name="John",
            last_name="Smith",
            position="head_chef",
            years_of_experience=10
        )
        Cook.objects.create(
            username="Devil",
            first_name="Bob",
            last_name="Bobson",
            position="line_cook",
            years_of_experience=12
        )
        Cook.objects.create(
            username="Angel",
            first_name="Jack",
            last_name="Jackson",
            position="prep_cook",
            years_of_experience=3
        )

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_uses_correct_context(self):
        response = self.client.get(COOK_URL)
        self.assertTemplateUsed(response, "kitchen_board/cook_list.html")
        self.assertIn("search_form", response.context)

    def test_list_cook_type(self):
        response = self.client.get(COOK_URL)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "God")
        self.assertContains(response, "Devil")
        self.assertContains(response, "Angel")

    def test_list_cook_search_by_username(self):
        response = self.client.get(COOK_URL, {"username": "vi"})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "God")
        self.assertContains(response, "Devil")
        self.assertNotContains(response, "Angel")

    def test_search_with_no_match(self):
        response = self.client.get(COOK_URL, {"username": "ma"})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "God")
        self.assertNotContains(response, "Devil")
        self.assertNotContains(response, "Angel")
        self.assertContains(response,
                            "There are no cooks on the Kitchen Board.",
                            html=True)

    def test_create_cook(self):
        form_data = {
            "username": "Valkyrie",
            "password1": "1234pass",
            "password2": "1234pass",
            "first_name": "Janny",
            "last_name": "Johnson",
            "position": "saucier",
            "years_of_experience": 9,
        }
        response = self.client.post(
            reverse("kitchen_board:cook_create"),
            data=form_data,
        )
        self.assertEqual(response.status_code, 302)
        new_cook = Cook.objects.get(username="Valkyrie")
        self.assertRedirects(response, reverse(
            "kitchen_board:cook_detail",
            kwargs={"pk": new_cook.pk})
                             )
        exists = Cook.objects.filter(username="Valkyrie").exists()
        self.assertTrue(exists)

    def test_update_cook(self):
        cook = Cook.objects.get(username="God")
        response = self.client.post(
            reverse(
                "kitchen_board:cook_update",
                kwargs={"pk": cook.pk}
            ),
            {
                "position": "pastry_chef",
                "years_of_experience": 15
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,  reverse(
            "kitchen_board:cook_detail",
            kwargs={"pk": cook.pk})
                             )
        cook.refresh_from_db()
        self.assertEqual(cook.position, "pastry_chef")
        self.assertEqual(cook.years_of_experience, 15)

    def test_delete_cook(self):
        cook = Cook.objects.get(username="Devil")
        response = self.client.post(
            reverse(
                "kitchen_board:cook_delete",
                kwargs={"pk": cook.pk}
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, COOK_URL)
        exists = Cook.objects.filter(username="Devil").exists()
        self.assertFalse(exists)

    def test_detail_dish(self):
        cook = Cook.objects.get(username="Angel")
        response = self.client.get(
            reverse(
                "kitchen_board:cook_detail",
                kwargs={"pk": cook.pk}
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, cook.username)
        self.assertTemplateUsed(response, "kitchen_board/cook_detail.html")
        self.assertEqual(response.context["cook"], cook)
