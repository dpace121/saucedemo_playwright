import re
from playwright.sync_api import Page, expect


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
        self.item_names = page.locator(".inventory_item_name")
        self.item_prices = page.locator(".inventory_item_price")
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")

    # ---------- checks ----------
    def expect_loaded(self):
        expect(self.page).to_have_url(re.compile(r".*/inventory\.html"))
        expect(self.title).to_have_text("Products")

    def expect_cart_count(self, count: int):
        if count == 0:
            expect(self.cart_badge).to_be_hidden()
        else:
            expect(self.cart_badge).to_have_text(str(count))

    # ---------- actions ----------
    def _item(self, item_name: str):
        return self.page.locator(".inventory_item").filter(has_text=item_name)

    def add_item_to_cart(self, item_name: str):
        self._item(item_name).get_by_role("button", name="Add to cart").click()

    def remove_item(self, item_name: str):
        self._item(item_name).get_by_role("button", name="Remove").click()

    def sort_by(self, option: str):
        """option: 'az', 'za', 'lohi', or 'hilo'"""
        self.sort_dropdown.select_option(option)

    def go_to_cart(self):
        self.cart_link.click()

    def logout(self):
        self.menu_button.click()
        self.logout_link.click()

    # ---------- data ----------
    def get_prices(self) -> list[float]:
        texts = self.item_prices.all_inner_texts()
        return [float(t.replace("$", "")) for t in texts]

    def get_names(self) -> list[str]:
        return self.item_names.all_inner_texts()