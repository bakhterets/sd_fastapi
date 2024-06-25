from unittest import TestCase


class HelloWorldTestCase(TestCase):
    
    def test_hello_world(self):
        result = hello_world()
        self.assertEqual(result, "Hello World")

def hello_world():
    return "Hello World"
