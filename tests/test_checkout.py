import pytest


def test_complete_checkout(at_checkout):
    at_checkout.fill_information("John", "Doe", "44600")
    at_checkout.expect_overview_loaded()
    at_checkout.expect_totals(
        subtotal="$29.99",
        tax="$2.40",
        total="$32.39",
    )
    at_checkout.finish()
    at_checkout.expect_order_complete()


@pytest.mark.parametrize("first, last, postal, error", [
    ("", "Doe", "44600", "First Name is required"),
    ("John", "", "44600", "Last Name is required"),
    ("John", "Doe", "", "Postal Code is required"),
])
def test_checkout_validation(at_checkout, first, last, postal, error):
    at_checkout.fill_information(first, last, postal)
    at_checkout.expect_error(error)