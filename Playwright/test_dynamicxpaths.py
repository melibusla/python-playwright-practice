from playwright.sync_api import Page, expect
import re
'''
Xpath
//button[text()='START' or text()='STOP']
//button[@name='start' or @name='stop']
//button[contains(@name, 'st')]
//button[starts-with(@name, 'st')]
//button[contains(@name, 'st')]
-----------
CSS
button[name='start'], button[name='stop']
ALT+94 = ^
button[name^='st'] = starts-with
button[name*='st'] = contains
-----------
Playwright

'''

def test_dynamic_elements(page:Page):
        page.goto("https://testautomationpractice.blogspot.com")

        for i in range(5):
            button = page.locator("//button[text()='START' or text()='STOP']")
            button.click()
            page.wait_for_timeout(2000)


def test_dynamic_elements_css(page: Page):
    page.goto("https://testautomationpractice.blogspot.com")

    for i in range(5):
        button = page.locator("button[name^='st']")
        button.click()
        page.wait_for_timeout(2000)

def test_dynamic_elements_pw(page: Page):
    page.goto("https://testautomationpractice.blogspot.com")

    for i in range(5):
        button = page.get_by_role("button", name=re.compile(r'ST.*'))
        button.click()
        page.wait_for_timeout(2000)