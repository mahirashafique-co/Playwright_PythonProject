from playwright.sync_api import Page, expect


def test_verify_page_url(page:Page):
    page.goto("https://testautomationu.applitools.com/")
    timeout = 60000
    verify_url=page.url
    print("this is page url",verify_url)

def test_verify_title_of_Webpage(page:Page):
    page.goto("https://testautomationu.applitools.com/")
    timeout = 60000
    expect(page).to_have_title("Test Automation University | Applitools")


def test_open_page_url_click_on_search(page:Page):
    page.goto("https://www.google.com/")
    search_box = page.locator("//*[@id='APjFqb']")
    search_box.fill("pakistan")
    search_box.press("Enter")