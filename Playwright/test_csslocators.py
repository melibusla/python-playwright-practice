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

def test_css_assignment(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    # Check logo
    expect(page.locator("img[alt='Tricentis Demo Web Shop']")).to_be_visible()
    # Search
    page.locator("#small-searchterms").fill("computer")
    page.locator("input[value='Search']").click()
    #page.wait_for_timeout(2000)
    # Count results
    products = page.locator("h2 > a[href*='computer']")
    print("Products count: ", products.count())
    expect(products).to_have_count(4)
    # Print name of the first product
    print("First Computer product:", products.first.text_content())
    # Print name of the last product
    print("Last Computer product:", products.last.text_content())
    # Print name of the nth product
    print("N-th Computer product:", products.nth(1).text_content())
    # Print titles of all the all products  (Tip: all_text_contents())
    #print("All products:", products.all()) #it prints the locators
    #print("All products:", products.all_text_contents())
    product_titles = products.all_text_contents()
    print("All computer related product names:", product_titles)

    for pt in product_titles:
        print(pt)
    # Get the fist. last and nth link from the footer section
    print("First link:", page.locator(".follow-us ul li:first-child").text_content())
    print("First link:", page.locator(".follow-us ul li:first-child a").get_attribute("href"))
    print("last link:", page.locator(".follow-us ul li:last-child").text_content())
    print("Last link:", page.locator(".follow-us ul li:last-child a").get_attribute("href"))
    print("Nth link:", page.locator(".follow-us ul li:nth-child(2)").text_content())
    print("Nth link:", page.locator(".follow-us ul li:nth-child(2) a").get_attribute("href"))