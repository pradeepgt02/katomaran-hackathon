from playwright.sync_api import sync_playwright
from pages.google_login_page import GoogleLoginPage
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    google = GoogleLoginPage(page)
    google.open()
    google.click_signin()
    popup = google.continue_with_google()
    popup.get_by_label("Email or phone").fill("pradeepkumarmswiss02@gmail.com")
    popup.get_by_role("button", name="Next").click()
    print(google.page.locator("body").inner_text())
    page.wait_for_timeout(5000)
    browser.close()