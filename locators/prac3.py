
from playwright.sync_api import Page,expect

def test_orghrm_login(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_timeout(2000)
    page.get_by_placeholder("Username").fill("Admin")
    page.wait_for_timeout(2000)
    page.get_by_placeholder("Password").fill("admin123")
    page.wait_for_timeout(2000)
    expect(page.get_by_placeholder("Username")).to_be_visible()
    expect(page.get_by_placeholder("Password")).to_be_visible()
    btn=page.get_by_role("Button" , name="Login")
    btn.click()
    page.wait_for_timeout(2000)
    page.get_by_role("Heading", name="Dashboard")
    expect(page.get_by_role("heading" , name="Dashboard")).to_be_visible()
    page.wait_for_timeout(3000)