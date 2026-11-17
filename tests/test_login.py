import pytest
from pages.inventory_page import InventoryPage

def test_valid_login(page, login_page):
    login_page.login("standard_user", "secret_sauce")
    InventoryPage(page).expect_loaded()
    
def test_locked_out_user(login_page):
    login_page.login("locked_out_user","secret_sauce")
    login_page.expect_error("this user has been locked out")
    
@pytest.mark.parametrize("username, password, error",[
    ("", "secret_sauce","Username is required"),
    ("standard_user","","Password is required"),
    ("wrong_user","wrong_pass","do not match"),      
])
def test_invalid_login(login_page, username, password, error):
    login_page.login(username, password)
    login_page.expect_error(error)