from product import Product
from product_manager import ProductManager
import random
from cart import Cart


def main():
    manager = ProductManager()

    manager.add_product(Product("Gejmerski Laptop", 799.99, 7))
    manager.add_product(Product("Bezicni mis", 19.99, 40))
    manager.add_product(Product("Bezicna tastatura", 55.50, 25))
    manager.add_product(Product("Monitor 27in", 199.9, 20))

    cart = Cart()
    selected_products = random.sample(manager.products, 3)
    for product in selected_products:
        cart.add_item(product)

    print("=== Sadrzaj korpe ===")
    cart.display_cart()
    print(f"\nUkupno za naplatu: {cart.calculate_total():.2f}")


if __name__ == "__main__":
    main()