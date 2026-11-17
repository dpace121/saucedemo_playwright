from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.cart_badge = page.locator(".shopping_cart_badge")
        
    def expect_loaded(self):
        expect(self.page).to_have_url("/inventory.html")
        expect(self.title).to_have_text("Products")
        
    def add_item_to_cart(self, item_name: str):
        item = self.page.locator(".inventory_item").filter(has_text = item_name)
        item.get_by_role("button", name="Add to cart").click()
        
    def expect_cart_count(self, count: int):
        expect(self.cart_badge).to_have_text(str(count))