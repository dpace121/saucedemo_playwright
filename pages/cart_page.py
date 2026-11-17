import re
from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.items = page.locator(".cart_item")
        self.checkout_button = page.locator('[data-test="checkout"]')
        self.continue_shopping_button = page.locator('[data-test="continue-shopping"]')

    def expect_loaded(self):
        expect(self.page).to_have_url(re.compile(r".*/cart\.html"))

    def expect_item_count(self, count: int):
        expect(self.items).to_have_count(count)

    def expect_item_present(self, item_name: str):
        expect(self.items.filter(has_text=item_name)).to_be_visible()

    def remove_item(self, item_name: str):
        self.items.filter(has_text=item_name).get_by_role("button", name="Remove").click()

    def checkout(self):
        self.checkout_button.click()

    def continue_shopping(self):
        self.continue_shopping_button.click()