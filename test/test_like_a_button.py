from pages.home_page import HomePage
from pages.buttons_page import ButtonsPage
from pages.like_a_button_page import LikeAButtonPage
import allure


@allure.feature('Like a button')
@allure.story('Existence')
def test_simple_button(browser):
    home_page = HomePage(browser)
    home_page.open()
    home_page.click_menu_buttons()
    buttons_page = ButtonsPage(browser)
    buttons_page.click_lika_a_button()
    like_a_button_page = LikeAButtonPage(browser)
    like_a_button_page.check_simple_like_a_button()


@allure.feature('Like a button')
@allure.story('Click ability')
def test_simple_button_page_title(browser):
    home_page = HomePage(browser)
    home_page.open()
    home_page.click_menu_buttons()
    like_a_button_page = LikeAButtonPage(browser)
    like_a_button_page.check_like_a_buttons_page_title("Looks like a button")
