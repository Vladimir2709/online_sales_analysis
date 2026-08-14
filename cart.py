class Cart:          # Predstavlja korpu kupca u onlone prodavnici.

    def __init__(self):
        self.cart_items = []

    def add_item(self, product):   # Dodaje prozivod u korpu.
        self.cart_items.append(product)

    def calculate_total(self):     # Racuna ukupnu vrednost za naplatu sadrzaja korpe.
        return sum(item.price for item in self.cart_items)

    def display_cart(self):        # Prikazuje sadrzaj korpe.
        if not self.cart_items:
            print("Korpa je prazna.")
            return
        for item in self.cart_items:
            item.display_info()
    
