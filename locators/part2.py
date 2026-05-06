from playwright.sync_api import Page , expect

#get by role
#get by label
#get by placeholder
#get by title
#get by test_id



def test_page_by_role(page:Page):

    page.goto("https://www.automationexercise.com/login")
    expect(page.get_by_role("heading", name="Login")).to_be_visible()

def test_page_label(page:Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.wait_for_timeout(7000)

    # get_by_label use karo
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.wait_for_timeout(2000)
    expect(page.get_by_label("Username")).to_be_visible()
    expect(page.get_by_label("Password")).to_be_visible()
    page.wait_for_timeout(2000)


def test_page_by_title(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_title("Home page link")).to_have_text("Home")
    expect(page.get_by_title("HyperText Markup Language")).to_have_text("HTML")
    page.wait_for_timeout(2000)


def test_page_by_test_id(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    page.wait_for_timeout(2000)
    expect(page.get_by_test_id("nav-home")).to_be_visible()
    expect(page.get_by_test_id("profile-name")).to_have_text("John Doe")
    page.wait_for_timeout(2000)
