from playwright.sync_api import sync_playwright
from pages.forgot_password_page import ForgotPasswordPage
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    forgot = ForgotPasswordPage(page)
    forgot.open()
    forgot.click_signin()
    forgot.wait(2000)
    forgot.enter_email("pradeepkumarmswiss02@gmail.com")
    forgot.click_continue()
    forgot.click_forgot_password()
    forgot.wait(1000)
    forgot.send_verification()
    forgot.wait(3000)
    print(forgot.get_url())
    print(forgot.get_title())
    print(forgot.page.locator("body").inner_text())
    browser.close()