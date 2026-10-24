# Pre requisite for async execution
# Install pytest_asyncio
# command: pip install pytest-asyncio
from playwright.async_api import async_playwright, Page, expect
import pytest

@pytest.mark.asyncio
async def test_verifyPageURL():
   async with async_playwright() as p:
        browser = await p.chromium.launch()
        newpage = await browser.new_page()
        await newpage.goto("https://demowebshop.tricentis.com/")
        print("Site URL: ", newpage.url)

        await expect(newpage).to_have_url("https://demowebshop.tricentis.com/")
        await browser.close()

