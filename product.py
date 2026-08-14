class Product:                 # Predstavalja jedan proizvod u online prodavnici
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):    # Prikazuje informacije o proizvodu.
        print(f"Naziv: {self.name} | Cena: {self.price:.2f} | Kolicina: {self.quantity}") 

    def update_quantity(self, new_quantity):  # Azurira kolicinu proizvoda na stanju.
        self.quantity = new_quantity



