from pages.base_page import BasePage
class SignupPage(BasePage):
    def click_signin(self):
        self.page.click("text=Sign In")
    def enter_email(self, email):
        self.page.fill('input[type="email"]', email)
    def click_continue(self):
        self.page.click("button:has-text('Continue')")
    def enter_first_name(self, first_name):
        self.page.get_by_placeholder("Enter your first name").fill(first_name)
    def enter_last_name(self, last_name):
        self.page.get_by_placeholder("Enter your last name").fill(last_name)
    def enter_phone(self, phone):
        self.page.get_by_placeholder("Enter your phone number").fill(phone)
    def enter_password(self, password):
        self.page.get_by_placeholder("Enter your password").fill(password)
    def enter_confirm_password(self, password):
        self.page.get_by_placeholder("Enter your confirm password").fill(password)
    def accept_terms(self):
        self.page.locator('button[role="checkbox"]').click()
    def click_signup(self):
        self.page.get_by_role("button", name="Sign Up").click()