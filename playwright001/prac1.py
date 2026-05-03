from playwright.sync_api import Page,expect


def test_amazon_page_search(page:Page):
    page.goto("https://www.amazon.com/")
    page.locator("//input[@id='twotabsearchtextbox']").fill("bags")
    page.locator("//input[@id='nav-search-submit-button']").click()



