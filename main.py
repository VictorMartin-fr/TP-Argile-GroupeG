def HelloWorld():
    return("Hello world")

def get_price():
    # On demande à l'utilisateur de saisir le prix unitaire de l'article
    price = input("Veuillez saisir le prix unitaire de l'article : ")
    
    # On convertit la valeur saisie en nombre à virgule flottante
    price = float(price)
    
    # On retourne le prix
    return price

def get_quantity():
    # On demande à l'utilisateur de saisir la quantité d'articles souhaitée
    quantity = input("Veuillez saisir la quantité d'articles souhaitée : ")
    
    # On convertit la valeur saisie en entier
    quantity = int(quantity)
    
    # On retourne la quantité
    return quantity

def get_total_price(price, quantity):
    # On calcule le prix total en multipliant le prix unitaire par la quantité
    total_price = price * quantity
    
    # On retourne le prix total
    return total_price
