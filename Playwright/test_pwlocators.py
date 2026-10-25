import re

from playwright.sync_api import Page, expect


def test_verify_pwlocators(page:Page):
   page.goto("http://localhost:8080")
   # 2s
   #page.wait_for_timeout(2000)

   #get_by_alt_text()
   logo = page.get_by_alt_text("nopCommerce demo store")
   expect(logo).to_be_visible()

   #get_by_text()
   expect(page.get_by_text("Welcome to our store")).to_be_visible() #full text
   expect(page.get_by_text("Welcome to")).to_be_visible() #partial text
   expect(page.get_by_text(re.compile(".*Welcome.*"))).to_be_visible() #partial with regular expression

   #get_by_role()
   page.goto("http://localhost:8080/register?returnUrl=%2F")
   #page.wait_for_timeout(2000)
   headingRegister = page.get_by_role("heading", name="Register")
   expect(headingRegister).to_be_visible()

   #get_by_label()
   page.get_by_label("First name:"). fill("John")
   page.get_by_label("Last name:"). fill("Doe")
   page.get_by_label("Email:"). fill("jdoe@gmail.com.ar")
   #page.wait_for_timeout(2000)

   #get_by_placeholder()
   page.get_by_placeholder("Search store").fill("Apple")
   #page.wait_for_timeout(2000)

   #get_by_title()
   page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
   expect(page.get_by_title("Home page link")).to_have_text("Home")
   expect(page.get_by_title("Hypertext Markup Language")).to_have_text("HTML")
   page.wait_for_timeout(2000)

   #get_by_test_id()
   expect(page.get_by_test_id("profile-name")).to_have_text("John Doe")
   expect(page.get_by_test_id("profile-email")).to_have_text("john.doe@example.com")
   page.close()

def test_login_assignment(page:Page):
   page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
   page.wait_for_timeout(2000)
   page.get_by_placeholder("Username").fill("Admin")
   page.get_by_placeholder("Password").fill("admin123")
   page.get_by_role("button", name="Login").click()
   expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
   page.close()