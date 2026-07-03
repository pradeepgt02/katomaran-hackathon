from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    invalid=LoginPage(page)
    invalid.open()
    invalid.click_signin()
    invalid.enter_email("pradeepkumarmswss02gmail.com")
    invalid.click_continue()
    print("Invalid email id")
    print(invalid.page.locator("body").inner_text())
    invalid.wait(2000)

