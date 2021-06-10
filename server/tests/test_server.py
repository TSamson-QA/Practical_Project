from flask import url_for
from flask_testing import TestCase
import requests_mock
from unittest.mock import patch

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_class(self):
        with patch('random.choice') as test_class:
            test_class.return_value = 'Human'
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(b'Human', response.data)
