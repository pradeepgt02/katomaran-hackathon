from pages.base_page import BasePage
class LoginPage(BasePage):
    def click_signin(self):
        self.page.click("text=Sign In")
    def enter_email(self, email):
        self.page.fill('input[type="email"]', email)
    def click_continue(self):
        self.page.click("button:has-text('Continue')")
    def enter_password(self, password):
        self.page.fill('input[type="password"]', password)
    def click_login(self):
        self.page.click("text=Login")