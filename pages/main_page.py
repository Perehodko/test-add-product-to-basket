from .base_page import BasePage
from selenium.webdriver.common.by import By
import math
from selenium.common.exceptions import NoAlertPresentException
import time
from .locators import BasePageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage): 
    def go_to_basket_button(self):
       login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
       login_link.click() 
   
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        print(answer)
        time.sleep(1)
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_correct_text_on_button(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK)

    def should_be_congrats_about_add_item_to_basket(self):
        name_of_book_in_basket = self.browser.find_element(*BasePageLocators.NAME_OF_BOOK_IN_BASKET)
        name_of_book = self.browser.find_element(*BasePageLocators.NAME_OF_BOOK)
        assert name_of_book_in_basket.text == name_of_book.text, "Name isn't correct"

    def should_be_correct_price(self):
        price_book = self.browser.find_element(*BasePageLocators.PRICE_BOOK)
        price_book_in_basket = self.browser.find_element(*BasePageLocators.PRICE_BOOK_IN_BASKET)
        assert price_book.text == price_book_in_basket.text, "Price isn't correct"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasePageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def should_be_correct_url(self):
        CORRECT_LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/" 
        assert self.browser.current_url == CORRECT_LOGIN_URL, "URL is not correct"

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        link.click()
        
    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasePageLocators.BASKET_EMPTY_MESSAGE), "Message about empty basket isn't present"

