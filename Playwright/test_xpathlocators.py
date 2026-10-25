from playwright.sync_api import Page, expect

def test_xpath_locators(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    # Absolute Xpath/full xpath
    logo = page.locator("//html/body/div[4]/div[1]/div[1]/div[1]/a/img")
    expect(logo).to_be_visible()

    # Relative Xpath: //tagname[@attribute='value']
    expect(page.locator("//img[@alt='Tricentis Demo Web Shop']")).to_be_visible()

    # Xpath with contains()
    products = page.locator("//h2//a[contains(@href, 'computer')]")
    products_count = products.count()
    expect(products).to_have_count(products_count)
    expect(products).to_have_count(4)

    print("First computer related product:", products.first.text_content())
    print("Last computer related product:", products.last.text_content())
    print("Nth computer related product:", products.nth(2).text_content())

    # Xpath with starts-with()
    building_products = page.locator("//h2//a[starts-with(@href, '/build')]")
    print("Count of Building Products:", building_products.count())
    expect(building_products).to_have_count(building_products.count())

    # Xpath with text() => inner text of the element
    # <input text = "xyz"> VS <input name="abc">Welcome!</>
    reg_link = page.locator("//a[text()='Register']")
    expect(reg_link).to_be_visible()

    # Xpath with last()
    google_link = page.locator("//div[@class='column follow-us']//li[last()]")
    #//div[@class='column follow-us']//li[3]
    expect(google_link).to_be_visible()
    expect(google_link).to_have_text("Google+")

    # Xpath with position()
    twitter_link = page.locator("//div[@class='column follow-us']//li[position()=2]")
    expect(twitter_link).to_have_text("Twitter")
