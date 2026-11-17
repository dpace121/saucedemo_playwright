import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def login_page(page):
    login = LoginPage(page)
    login.open()
    return login


@pytest.fixture
def logged_in(page, login_page):
    """Logged in and on the inventory page."""
    login_page.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.expect_loaded()
    return inventory


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)


@pytest.fixture
def at_checkout(logged_in, cart_page, checkout_page):
    """One backpack in the cart, sitting on the checkout information form."""
    logged_in.add_item_to_cart("Sauce Labs Backpack")
    logged_in.go_to_cart()
    cart_page.checkout()
    return checkout_page