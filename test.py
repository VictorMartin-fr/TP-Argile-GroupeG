import unittest
import sys
from io import StringIO

from main import HelloWorld
from main import get_total_price
from main import print_price

class test(unittest.TestCase):
    def test_hello_world(self):
        # On vérifie que la fonction "hello_world" retourne bien la chaîne de caractères "Hello world"
        self.assertEqual(HelloWorld(), "Hello world")

    def test_get_total_price(self):
        # On vérifie que la fonction "get_total_price" retourne bien le prix total en multipliant le prix unitaire par la quantité
        self.assertEqual(get_total_price(10, 5), 50)
        self.assertEqual(get_total_price(20, 3), 60)
        self.assertEqual(get_total_price(100, 1), 100)

    def test_print_price(self):
        # On redirige la sortie standard vers un buffer pour pouvoir vérifier le message affiché
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        # On appelle la fonction "print_price" avec différents prix d'article
        print_price(10)
        print_price(20)
        print_price(30)
        
        # On récupère le contenu du buffer et on le compare aux messages attendus
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "Le prix de l'article est de 10 euros\nLe prix de l'article est de 20 euros\nLe prix de l'article est de 30 euros")
        
        # On rétablit la sortie standard
        sys.stdout = old_stdout



if __name__ == "__main__":
    unittest.main()