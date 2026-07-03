from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    login = LoginPage(page)
    login.open()
    login.click_signin()
    login.wait(2000)
    login.enter_email("pradeepkumarmswiss02@gmail.com")
    login.click_continue()
    login.wait(2000)
    login.enter_password("Pnex@gt2")
    login.click_login()
    login.wait(5000)
    print(login.get_url())
    print(login.get_title())
    print(login.page.locator("body").inner_text())
    browser.close()