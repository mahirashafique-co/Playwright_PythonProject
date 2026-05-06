from playwright.sync_api import Page, expect

def test_pract_day3(page:Page):
    page.goto("https://www.automationexercise.com/login")
    page.wait_for_timeout(2000)
    hed=page.get_by_role("heading" , name="Login to your account")
    expect(hed).to_be_visible()
    print(hed.text_content())
    page.wait_for_timeout(2000)
    eme=page.get_by_placeholder("Email Address").first
    eme.fill("mahira.shafique@hotmail.com")
    expect(eme).to_be_visible()
    page.wait_for_timeout(2000)
    page.get_by_placeholder("Password").fill("tst")
    expect(page.get_by_placeholder("Password")).to_be_visible()
    page.wait_for_timeout(2000)
    butt=page.get_by_role("button", name="login")
    butt.click()
    expect(butt).to_be_visible()
    page.wait_for_timeout(2000)



