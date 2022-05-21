import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..","."))
import time
from Pages.Homepage import HomePage
from Pages.Productpageapple import ProductPageApple
from Pages.cart import CartPage
#from Pages.cart import CartPage

class BuyTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.s = Service(r"C:\Users\Dawid\.wdm\drivers\chromedriver\win32\101\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=cls.s)
        cls.driver.maximize_window()
    
    def test_01_url_apple_monitor(self):
        driver = self.driver
        driver.get("https://www.demoblaze.com/index.html")
        home_page = HomePage(driver)
        home_page.pick_monitor_tab()
        home_page.pick_apple_monitor_24()

        get_url = self.driver.current_url
        self.assertEqual(get_url, 'https://www.demoblaze.com/prod.html?idp_=10')
        
        ProductPageApple(driver).wait_for_monitor_img_load()
        driver.save_screenshot(r'C:\Python\Testing\reports\screenshots\Apple.png')
    
    def test_02_name_and_price_apple(self):
        driver = self.driver
        product_page_apple = ProductPageApple(driver)
        self.assertEqual(product_page_apple.get_monitor_name(), 'Apple monitor 24')
        self.assertEqual(product_page_apple.get_monitor_price(), '$400')
        product_page_apple.add_to_cart()
        product_page_apple.wait_for_alert()
        self.assertEqual(product_page_apple.get_alert_text(), 'Product added')
        product_page_apple.accept_alert()
        
        #go to cart
        HomePage(driver).go_to_cart()
       
        ###cart page
        self.assertEqual(CartPage(driver).get_header(), 'Products')

        self.assertEqual(CartPage(driver).check_if_product_apple_exist(), 'Apple monitor 24')
        
        self.assertEqual(CartPage(driver).check_cart_price(), '400')

        CartPage(driver).click_button_cart()
        #self.driver.find_element(By.CSS_SELECTOR,'.btn.btn-success').click()
        time.sleep(5)
        
        
        

        
        # print(alert.text)
        # alert.accept()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
    
if __name__ =='__main__':
    unittest.main()


#options = webdriver.ChromeOptions()




