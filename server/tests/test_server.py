from flask import url_for
from flask_testing import TestCase
import requests_mock

from app import app

class TestBase(TestCase):
    def create_app(self):
        
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        db.create_all()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()
    
    def test_home(self):
        with requests_mock.Mocker() as mocker:
            mocker.get('http://class_api:5001/get_class', text='Druid')
            mocker.get('http://race_api:5002/get_race', text='Human')
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'The generated character is a Human Druid with an alignment of True Neutral', response.data)
    
