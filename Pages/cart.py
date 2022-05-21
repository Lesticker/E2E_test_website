from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.locators import Locators

class CartPage():

    def __init__(self, driver):
        self.driver = driver
    
    def get_header(self):
        cart_header_text = self.driver.find_elements(*Locators.cart_header)[0].text
        return cart_header_text
    
    def check_if_product_apple_exist(self):
        cart_title = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((Locators.cart_title_x))).text
        return cart_title
    
    def check_cart_price(self):
        cart_price = self.driver.find_element(*Locators.cart_price_x).text
        return cart_price

    def click_button_cart(self):
        self.driver.find_element(*Locators.button_cart).click()
