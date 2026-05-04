import re

from playwright.sync_api import Page ,expect
import time



#get_by_alt_text() yah use hota like image k alt text k liye
#get_by_text() visible text content
#get_by_role()

def test_logo_of_page(page:Page):
    page.goto("https://demo.nopcommerce.com/")
    time.sleep(5)# yah python ko hold kre ga
    page.wait_for_timeout(5000)  # yah browser ko hold krta hai using playwright
    logo= page.get_by_alt_text("nopCommerce demo store")
    expect(logo).to_be_visible()
    welcome_text=page.get_by_text(re.compile(".*Welcome.*"))
    print(welcome_text.text_content())
    expect(welcome_text).to_be_visible()
    #expect(page.get_by_text(re.compile("Welcome"))).to_be_visible()
    #print(expect(page.get_by_text(re.compile("Welcome"))).to_be_visible())
    page.close()


