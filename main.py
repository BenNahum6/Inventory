from source import inventory, product

if __name__ == "__main__":
    # Create products
    product1 = product.Product("Appl", 2.9, 5)
    product2 = product.Product("Banana", 5.66, 10)
    product3 = product.Product("Watermelon", 25.2, 7)

    # Create inventory instance and products to inventory
    inventory = inventory.Inventory()

    # Add product to inventory
    inventory.add_product(product1)
    inventory.add_product(product2)
    inventory.add_product(product3)

    # Retrieve and display a product
    product = inventory.get_product("Appl")
    print(product if product else "Product not found.")
    product = inventory.get_product("Mengo")
    print(product if product else "Product not found.")

    # Remove a product and display inventory value
    print(inventory.total_inventory_value())
    inventory.remove_product("Keyboard")
    print("Total inventory value:", inventory.total_inventory_value())
    inventory.remove_product("Appl")
    print("Total inventory value:", inventory.total_inventory_value())