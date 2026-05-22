from django.test import TestCase


class RegistrationTestCase(TestCase):

    def test_user_account_is_create(self):
        self.client.post(
            '/users/register',
            data={
                'username': 'admin1',
                'first_name': 'admin1',
                'last_name': 'admin1',
                'email': 'admin1@gmail.com',
                'password': 'password'
            }
        )
