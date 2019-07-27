from pages.main_page import MainPage
import time


def test_guest_can_click_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_basket_button()       # выполняем метод страницы - переходим на страницу логина
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.should_be_congrats_about_add_item_to_basket()
    page.should_be_correct_price()

def test_guest_should_see_correct_text_on_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)
    page.open()
    page.should_be_correct_text_on_button()
