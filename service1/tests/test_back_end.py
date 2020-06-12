import unittest

from flask import url_for
from flask_testing import TestCase

from application import app
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        return app


class TestViews(TestBase):

    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 500)
        with self.client:
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 500)