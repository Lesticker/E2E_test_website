from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from Pages.locators import Locators


class ProductPageApple():

    def __init__(self, driver):
        self.driver = driver
        self.monitor_img = Locators.monitor_img
        self.product_name = Locators.product_name
        self.product_price = Locators.product_price
        
    
    def wait_for_monitor_img_load(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((Locators.monitor_img)))
    
    def get_monitor_name(self):
        l = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((Locators.product_name)))
        s= l.text
        return s
    
    def get_monitor_price(self):
        l= self.driver.find_element(*Locators.product_price).get_attribute('innerHTML').strip('<small> *includes tax</small>')
        return l
    
    def add_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, '.btn.btn-success.btn-lg').click()
    
    def wait_for_alert(self):
        WebDriverWait(self.driver, 20).until(EC.alert_is_present())
    
    def get_alert_text(self):
        alert_text = Alert(self.driver).text
        return alert_text
    
    def accept_alert(self):
        Alert(self.driver).accept()
    