from flask import url_for
from flask_testing import TestCase
import requests_mock

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as mocker:
            mocker.get('http://class_api:5001/get_class', text='Cleric')
            mocker.get('http://race_api:5002/get_race', text='Dwarf')
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'The generated character is a Dwarf Cleric with an alignment of Lawful Good', response.data)