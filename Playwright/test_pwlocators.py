from playwright.sync_api import Page, expect


def test_verify_pwlocators(page:Page):
   page.goto("http://localhost:8080")
   logo = page.get_by_alt_text("nopCommerce demo store")
   expect(logo).to_be_visible()

