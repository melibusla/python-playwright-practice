from playwright.sync_api import Page, expect

def test_verifyPageURL(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    # Capture the url and print it
    siteUrl = page.url
    print("Site URL: ", siteUrl)
    #Assert
    expect(page).to_have_url("https://demowebshop.tricentis.com/")

def test_verifyPageTitle(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    # Capture the title and print it
    siteTitle = page.title()
    print("Title of the site: ", siteTitle)
    expect(page).to_have_title("Demo Web Shop")