from product import Product
from product_manager import ProductManager
import random
from cart import Cart


def main():
    manager = ProductManager()


    manager.add_product(Product("Laptop", 799.99, 5))
    manager.add_product(Product("Bezicni mis", 19.99, 50))
    manager.add_product(Product("Mehanicka tastatura", 55.50, 30))
    manager.add_product(Product("Monitor 24in", 199.9, 20))


    print("=== Lista proizvoda ===")
    manager.display_products()

    print(f"\nUkupna vrednost imventara: {manager.total_inventory_value():.2f}")
    print()


    cart = Cart()
    selected_products = random.sample(manager.products, 3)
    for product in selected_products:
        cart.add_item(product)

    print("=== Sadrzaj korpe ===")
    cart.display_cart()
    print(f"\nUkupno za naplatu: {cart.calculate_total():.2f}")



if __name__ == "__main__":
    main()