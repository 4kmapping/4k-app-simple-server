from django.test import TestCase
from django.contrib.auth.models import User
from tastypie.test import ResourceTestCase
from mapi.models import Location

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


