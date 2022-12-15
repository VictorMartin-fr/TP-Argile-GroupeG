import unittest
from main import HelloWorld
from main import get_total_price

class test(unittest.TestCase):
    def test_hello_world(self):
        # On vérifie que la fonction "hello_world" retourne bien la chaîne de caractères "Hello world"
        self.assertEqual(HelloWorld(), "Hello world")

    def test_get_total_price(self):
        # On vérifie que la fonction "get_total_price" retourne bien le prix total en multipliant le prix unitaire par la quantité
        self.assertEqual(get_total_price(10, 5), 50)
        self.assertEqual(get_total_price(20, 3), 60)
        self.assertEqual(get_total_price(100, 1), 100)



if __name__ == "__main__":
    unittest.main()