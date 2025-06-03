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
