import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def login_page(page):
    login = LoginPage(page)
    login.open()
    return login

@pytest.fixture
def logged_in(page, login_page):
   """Logs in and returns the inventory page, ready to use."""
   login_page.login("standard_user", "secret_sauce")
   inventory = InventoryPage(page)
   inventory.expect_loaded()
   return inventory 