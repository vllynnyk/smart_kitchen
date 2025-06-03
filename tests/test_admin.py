from django.contrib.auth import get_user_model
from django.test import TestCase, Client


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
