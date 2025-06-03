from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_superuser(
            username="admin",
            password="1234pass"
        )
        self.cook = get_user_model().objects.create_user(
            username="cook",
            password="1234pass",
            position="head_chef",
            years_of_experience=2
        )

    def test_admin_available_for_is_staff(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("admin:index"))
        self.assertTrue(self.user.is_staff)
        self.assertEqual(response.status_code, 200)

    def test_admin_available_for_is_not_staff(self):
        self.client.force_login(self.cook)
        response = self.client.get(reverse("admin:index"))
        self.assertFalse(self.cook.is_staff)
        self.assertNotEqual(response.status_code, 200)

    def test_cook_additional_fields(self):
        self.client.force_login(self.user)
        url = reverse("kitchen_board:cook_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.cook.get_position_display())
        self.assertContains(response, self.cook.years_of_experience)

    def test_cook_additional_fields_admin(self):
        self.client.force_login(self.user)
        url = reverse("kitchen_board:cook_detail", args=[self.cook.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.cook.get_position_display())
        self.assertContains(response, self.cook.years_of_experience)

    def test_create_cook_via_admin(self):
        self.client.force_login(self.user)
        url = reverse("admin:kitchen_board_cook_add")
        data = {
            "username": "God",
            "password1": "1234pass",
            "password2": "1234pass",
            "first_name": "John",
            "last_name": "Smith",
            "position": "head_chef",
            "years_of_experience": 10,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        new_cook = get_user_model().objects.get("God")
        self.assertEqual(new_cook.position, "head_chef")
        self.assertEqual(new_cook.years_of_experience, 10)

    def test_update_cook_position_via_admin(self):
        self.client.force_login(self.user)
        url = reverse("admin:kitchen_board_cook_change", args=[self.cook.id])
        data = {
            "username": self.cook.username,
            "date_joined_0": self.cook.date_joined.strftime("%Y-%m-%d"),
            "date_joined_1": self.cook.date_joined.strftime("%H:%M:%S"),
            "position": "pastry_chef",
            "years_of_experience": 8,
        }
        response = self.client.post(url, data)
        if response.status_code != 302:
            print(response.content.decode())
        self.assertEqual(response.status_code, 302)
        self.cook.refresh_from_db()
        self.assertEqual(self.cook.position, "pastry_chef")
        self.assertEqual(self.cook.years_of_experience, 8)
