from source import product


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, prod: product):
        """
        Adds a product to inventory if the values entered are correct. If the product exists, updates the quantity.
        :param prod:
        :return: None
        """
        if not isinstance(prod.name, str):
            return False
        if not isinstance(prod.price, (int, float)) or prod.price <= 0:
            return False
        if not isinstance(prod.quantity, int) or prod.quantity <= 0:
            return False
        if prod.name in self.products:
            self.products[prod.name].quantity += prod.quantity
        else:
            self.products[prod.name] = prod

    def remove_product(self, product_name: str):
        """
        Removes a product by name if it exists.
        :param product_name:
        :return: None
        """
        if product_name in self.products:
            del self.products[product_name]
            print(f"Product '{product_name}', removed from inventory.")
        else:
            print(f"Product '{product_name}', not found in inventory.")

    def get_product(self, product_name: str) -> product:
        """
        fine the product by name and return the prod else Returns None.
        :param product_name:
        :return: product name or None
        """
        if product_name in self.products:
            return self.products.get(product_name, None)

    def total_inventory_value(self) -> float:
        """
        Calculates the total value of the inventory.
        :return: total value
        """
        total_value = 0.0
        for prod in self.products.values():
            total_value += prod.price * prod.quantity
        return total_value
