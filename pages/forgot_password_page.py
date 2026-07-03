from pages.base_page import BasePage
class ForgotPasswordPage(BasePage):
    def click_signin(self):
        self.page.click("text=Sign In")
    def enter_email(self, email):
        self.page.get_by_placeholder("Enter your email address").fill(email)
    def click_continue(self):
        self.page.click("button:has-text('Continue')")
    def click_forgot_password(self):
        self.page.click("text=Forgot Password")
    def send_verification(self):
        self.page.click("text=Send Verification")