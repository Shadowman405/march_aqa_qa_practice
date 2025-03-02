from selenium.webdriver.common.by import By


class HomePage:
    BASE_URL = 'https://www.qa-practice.com/'

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get(self.BASE_URL)

    def click_menu_buttons(self):
        button_link = self.browser.find_element(By.XPATH, '//a[text()="Simple button"]')
        button_link.click()

