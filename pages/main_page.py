from .base_page import BasePage
from selenium.webdriver.common.by import By
import math
from selenium.common.exceptions import NoAlertPresentException
import time


class MainPage(BasePage): 
    def go_to_basket_button(self):
       login_link = self.browser.find_element(By.XPATH, "//button [text()='Add to basket']")
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
        self.browser.find_element(By.XPATH, "//button [text()='Add to basket']")

    def should_be_congrats_about_add_item_to_basket(self):
        name_of_book_in_basket = self.browser.find_element(By.CSS_SELECTOR,"#messages > div:nth-child(1) > div > strong")
        name_of_book = self.browser.find_element(By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
        assert name_of_book_in_basket.text == name_of_book.text, "Name isn't correct"

    def should_be_correct_price(self):
        price_book = self.browser.find_element(By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
        price_book_in_basket = self.browser.find_element(By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
        assert price_book.text == price_book_in_basket.text, "Price isn't correct"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong"), \
       "Success message is presented, but should not be"


        
        



        



        
        




        
