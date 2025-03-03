from selenium.webdriver.common.by import By


class LikeAButtonPage:
    BASE_URL = 'https://www.qa-practice.com/elements/button/like_a_button'

    def __init__(self, browser):
        self.browser = browser

    def check_simple_like_a_button(self):
        assert self.browser.find_element(By.LINK_TEXT, 'Click').is_displayed()

    def check_like_a_buttons_page_title(self, title):
        page_title = self.browser.find_element(By.XPATH, '//*[@id="content"]/ul/li[2]/a')
        assert page_title.text == title
