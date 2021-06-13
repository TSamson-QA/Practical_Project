from flask import url_for
from flask_testing import TestCase

from alignment_app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_alignment(self):
        for _ in range(20):
            response = self.client.get(url_for('get_alignment'))
            self.assertIn(response.data.decode("utf-8"),['Lawful Good','Neutral Good', 'Chaotic Good', 'Lawful Neutral', 'True Neutral', 'Chaotic Neutral', 'Lawful Evil', 'Neutral Evil', 'Chaotic Evil'])
