from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_race(self):
        for _ in range(20):
            response = self.client.get(url_for('get_race'))
            self.assertIn(response.data,['Dwarf', 'Halfling', 'Elf', 'Gnome', 'Human', 'Half-Elf', 'Tiefling', 'Dragonborn', 'Half-Orc'])
