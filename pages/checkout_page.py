import re
from playwright.sync_api import Page, expect


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        # Step one: your information
        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.postal_code = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.error_message = page.locator(".error-message-container")
        # Step two: overview
        self.subtotal = page.locator(".summary_subtotal_label")
        self.tax = page.locator(".summary_tax_label")
        self.total = page.locator(".summary_total_label")
        self.finish_button = page.locator('[data-test="finish"]')
        # Complete
        self.complete_header = page.locator(".complete-header")

    # ---------- step one ----------
    def fill_information(self, first: str, last: str, postal: str):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(postal)
        self.continue_button.click()

    def expect_error(self, text: str):
        expect(self.error_message).to_contain_text(
            re.compile(re.escape(text), re.IGNORECASE)
        )

    # ---------- step two ----------
    def expect_overview_loaded(self):
        expect(self.page).to_have_url(re.compile(r".*/checkout-step-two\.html"))

    def expect_totals(self, subtotal: str, tax: str, total: str):
        expect(self.subtotal).to_contain_text(subtotal)
        expect(self.tax).to_contain_text(tax)
        expect(self.total).to_contain_text(total)

    def finish(self):
        self.finish_button.click()

    # ---------- complete ----------
    def expect_order_complete(self):
        expect(self.page).to_have_url(re.compile(r".*/checkout-complete\.html"))
        expect(self.complete_header).to_have_text("Thank you for your order!")