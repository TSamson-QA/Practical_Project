from flask import url_for
from flask_testing import TestCase

from app import class_app

class TestBase(TestCase):
    def create_app(self):
        return class_app

class TestHome(TestBase):
    def test_get_class(self):
        for _ in range(20):
            response = self.client.get(url_for('get_class'))
            self.assertIn(response.data,['Cleric', 'Fighter', 'Bard', 'Monk', 'Druid', 'Sorcerer', 'Warlock', 'Rogue', 'Barbarian'])
