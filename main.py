from product import Product
from product_manager import ProductManager

def main():
    manager = ProductManager()


    manager.add_product(Product("Gejmerski Laptop", 799.99, 7))
    manager.add_product(Product("Bezicni mis", 19.99, 40))
    manager.add_product(Product("Bezicna tastatura", 55.50, 25))
    manager.add_product(Product("Monitor 27in", 199.9, 20))


if __name__ == "__main__":
    main()