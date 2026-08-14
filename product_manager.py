from product import Product


class ProductManager:   # Upravlja kolekcijom proizvoda u prodavnici.

    def __init__(self):
        self.products = []

    def add_product(self, product):  # Dodaje novi proizvod u listu dostupnih proizvoda
        self.products.append(product)

    def remove_product(self, name):  # Uklanja proizvod iz liste na osnovu imena.
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"Proizvod '{name}' je uklonjen.")
                return
        print(f"Proizvod '{name}' nije pronadjen.")

    def display_products(self):      # Prikazuje sve dostupne proizvode.
        if not self.products:
            print("Nema dostupnih proizvoda.")
            return

        for product in self.products:
            product.display_info()


    def total_inventory_value(self):  # Racuna ukupnu vrednost svih proizvoda na stanju.
        return sum(p.price * p.quantity for p in self.products)