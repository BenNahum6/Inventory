import pytest
from source import inventory, product


@pytest.fixture
def test_inventory():
    inventory_instance = inventory.Inventory()
    first_product = product.Product("Appl", 4.2, 2)
    inventory_instance.add_product(first_product)
    return inventory_instance


def test_add_product(test_inventory):
    """
    Adds a new product to inventory.
    :param test_inventory:
    :return: True
    """
    first_product = product.Product("Asado", 78.65, 2)
    test_inventory.add_product(first_product)
    assert "Asado" in test_inventory.products


def test_multiple_tasks(test_inventory):
    """
    Checks that they actually exist, checks prices, checks quantity, and checks price.
    :param test_inventory:
    :return: True
    """
    product_one = product.Product("Appl", 4.2, 2)
    test_inventory.add_product(product_one)
    second_product = product.Product("Banana", 3.69, 5)
    test_inventory.add_product(second_product)
    theed_product = product.Product("Watermelon", 13.99, 1)
    test_inventory.add_product(theed_product)

    assert "Appl" in test_inventory.products
    assert test_inventory.products["Appl"].quantity == 4
    assert "Banana" in test_inventory.products
    assert test_inventory.products["Banana"].price == 3.69
    with pytest.raises(AssertionError, match="assertion failed as expected"):
        assert test_inventory.products["Banana"].price == 14.99, "assertion failed as expected"
    assert test_inventory.total_inventory_value()


def test_get_product(test_inventory):
    """
    Access an existing product.
    :param test_inventory:
    :return: True
    """
    product = test_inventory.get_product("Appl")
    assert product is not None
    assert product.name == "Appl"


def test_get_product_not_existing(test_inventory):
    """
    Trying to access a product that does not exist.
    :param test_inventory:
    :return: True
    """
    product = test_inventory.get_product("Lemon")
    assert product is None


def test_remove_product(test_inventory):
    """
    Deletes product from inventory.
    :param test_inventory:
    :return: True
    """
    product = test_inventory.get_product("Watermelon")
    test_inventory.remove_product(product)
    assert "Watermelon" not in test_inventory.products


def test_remove_product_not_existing(test_inventory, capfd):
    """
    Trying to delete a product that does not exist in inventory.
    :param test_inventory:
    :param capfd:
    :return: True
    """
    test_inventory.remove_product("Lemon")
    captured = capfd.readouterr()
    assert "Product 'Lemon', not found in inventory." in captured.out


def test_total_inventory_value(test_inventory):
    """
    Returns the total value of the inventory.
    :param test_inventory:
    :return: True
    """
    assert test_inventory.total_inventory_value()
