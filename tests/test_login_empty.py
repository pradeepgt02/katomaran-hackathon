from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    empty=LoginPage(page)
    empty.open()
    empty.click_signin()
    empty.click_continue()
    empty.wait(2000)
    print(empty.page.locator("body").inner_text())