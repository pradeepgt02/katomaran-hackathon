from pages.base_page import BasePage
class GoogleLoginPage(BasePage):
    def click_signin(self):
        self.page.click("text=Sign In")
    def continue_with_google(self):
        with self.page.expect_popup() as popup:
            self.page.click("text=Continue with Google")
        google = popup.value
        google.wait_for_load_state()
        return google