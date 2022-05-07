import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from Pages.Homepage import HomePage
from Pages.Productpageapple import ProductPageApple

class BuyTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.s = Service(r"C:\Users\Dawid\.wdm\drivers\chromedriver\win32\97.0.4692.71\chromedriver.exe")
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

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
    
if __name__ =='__main__':
    unittest.main()


#options = webdriver.ChromeOptions()




