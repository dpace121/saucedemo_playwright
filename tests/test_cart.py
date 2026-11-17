def test_add_one_item(logged_in):
    logged_in.add_item_to_cart("Sauce Labs Backpack")
    logged_in.expect_cart_count(1)


def test_add_two_items(logged_in):
    logged_in.add_item_to_cart("Sauce Labs Backpack")
    logged_in.add_item_to_cart("Sauce Labs Bike Light")
    logged_in.expect_cart_count(2)
    
def test_remove_item_from_inventory(logged_in):
    logged_in.add_item_to_cart("Sauce Labs Backpack")
    logged_in.remove_item("Sauce Labs Backpack")
    logged_in.expect_cart_count(0)


def test_cart_shows_added_items(logged_in, cart_page):
    logged_in.add_item_to_cart("Sauce Labs Backpack")
    logged_in.add_item_to_cart("Sauce Labs Bike Light")
    logged_in.go_to_cart()
    cart_page.expect_loaded()
    cart_page.expect_item_count(2)
    cart_page.expect_item_present("Sauce Labs Backpack")
    cart_page.expect_item_present("Sauce Labs Bike Light")


def test_remove_item_from_cart_page(logged_in, cart_page):
    logged_in.add_item_to_cart("Sauce Labs Backpack")
    logged_in.go_to_cart()
    cart_page.remove_item("Sauce Labs Backpack")
    cart_page.expect_item_count(0)