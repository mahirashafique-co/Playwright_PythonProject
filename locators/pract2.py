import re

from playwright.sync_api import Page, expect

def test_flip_card_search(page:Page):
    page.goto("https://www.flipkart.com")
    page.wait_for_timeout(7000)
    t1=page.get_by_placeholder("Search for Products, Brands and More").first
    t1.fill("mobile")
    page.keyboard.press("Enter")
    page.wait_for_timeout((5000))

    title= page.title()
    print(title)
    expect(page).to_have_title(re.compile(".*mobile*." , re.IGNORECASE))