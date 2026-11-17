def test_sort_price_low_to_high(logged_in):
    logged_in.sort_by("lohi")
    prices = logged_in.get_prices()
    assert prices == sorted(prices)


def test_sort_price_high_to_low(logged_in):
    logged_in.sort_by("hilo")
    prices = logged_in.get_prices()
    assert prices == sorted(prices, reverse=True)


def test_sort_name_a_to_z(logged_in):
    logged_in.sort_by("az")
    names = logged_in.get_names()
    assert names == sorted(names)


def test_sort_name_z_to_a(logged_in):
    logged_in.sort_by("za")
    names = logged_in.get_names()
    assert names == sorted(names, reverse=True)