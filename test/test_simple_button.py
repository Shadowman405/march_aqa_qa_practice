from pages.home_page import HomePage
from pages.buttons_page import ButtonsPage


def test_simple_button(browser):
    home_page = HomePage(browser)
    home_page.open()
    home_page.click_menu_buttons()
    buttons_page = ButtonsPage(browser)
    buttons_page.check_buttons_page_title("Buttons")
    buttons_page.check_simple_button()
