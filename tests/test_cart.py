def test_add_one_item(logged_in):
    logged_in.add_item_to_cart("Sauce Labs Backpack")
    logged_in.expect_cart_count(1)


def test_add_two_items(logged_in):
    logged_in.add_item_to_cart("Sauce Labs Backpack")
    logged_in.add_item_to_cart("Sauce Labs Bike Light")
    logged_in.expect_cart_count(2)