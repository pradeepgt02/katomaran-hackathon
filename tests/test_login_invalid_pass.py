from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    inpass=LoginPage(page)
    inpass.open()
    inpass.click_signin()
    inpass.wait(2000)
    inpass.enter_email("pradeepkumarmswiss02@gmail.com")
    inpass.click_continue()
    inpass.wait(2000)
    inpass.enter_password("Abcd12@3")
    inpass.click_login()
    print(inpass.page.locator("body").inner_text())
    inpass.wait(2000)