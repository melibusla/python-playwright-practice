from playwright.sync_api import Page, expect

'''
    tag id => tag#id
    tag class => tag.class
    tag attribute => tag[attribute=value]
    tag class attribute => tag.class[attribute=value]
'''



def test_verify_css_locators(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    #tag id
    #tag is optional in the sintaxis
    #page.locator("input#small-searchterms").fill("laptop")
    page.locator("#small-searchterms").fill("laptop")
    page.wait_for_timeout(2000)
    page.locator(".search-box-text").fill("laptop")
    #page.locator("input[name=q]").fill("laptop")
    page.locator("[name=q]").fill("laptop")
     #page.locator("input[name=q]").fill("laptop")
    page.locator("input.search-box-text[name=q]").fill("laptop")
    page.locator(".search-box-text[value='Search store']").fill("mac")