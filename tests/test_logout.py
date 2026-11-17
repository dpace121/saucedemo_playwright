from playwright.sync_api import expect


def test_logout_returns_to_login(logged_in, login_page):
    logged_in.logout()
    expect(login_page.login_button).to_be_visible()
    expect(login_page.username_input).to_be_empty()