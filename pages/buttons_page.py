from selenium.webdriver.common.by import By


class ButtonsPage:
    BASE_URL = 'https://www.qa-practice.com/elements/button/simple'

    def __init__(self, browser):
        self.browser = browser

    def check_simple_button(self):
        assert self.browser.find_element(By.ID, 'submit-id-submit').is_displayed()

    def click_lika_a_button(self):
        link_to_simple_buuton = self.browser.find_element(By.XPATH, '//a[text()="Looks like a button"]')
        link_to_simple_buuton.click()

    def check_buttons_page_title(self, title):
        page_title = self.browser.find_element(By.XPATH, '//*[@id="content"]/h1')
        assert page_title.text == title
