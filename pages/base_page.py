from playwright.sync_api import Page
class BasePage:
    def __init__(self, page: Page):
        self.page = page
    def open(self):
        self.page.goto("https://tichi-app-webapp-stage.web.app/")
    def get_url(self):
        return self.page.url
    def get_title(self):
        return self.page.title()
    def wait(self, ms):
        self.page.wait_for_timeout(ms)