from unittest import TestCase
from main import SimpleApplication


class TestSimpleApplication(TestCase):
    def test_print_message(self):
        self.app = SimpleApplication("Hello World")
        self.assertEqual(self.app.message, "Hello World")
