import unittest
from main import HelloWorld

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        # On vérifie que la fonction "hello_world" retourne bien la chaîne de caractères "Hello world"
        self.assertEqual(HelloWorld(), "Hello world")
        print("1")

if __name__ == "__main__":
    unittest.main()