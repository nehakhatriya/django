from django.test import TestCase
import os
from django.contrib.auth.password_validation import validate_password
class TryDjangoConfigTest(TestCase):

    def test_secretKey(self):
        secret_key=os.environ.get('SECRET_KEY')

        try:
            isStrong=validate_password(secret_key)
        except Exception as e:
            msg = f'Bad Secret Key'
            self.fail(msg)