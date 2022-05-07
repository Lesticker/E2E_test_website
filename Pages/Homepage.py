from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.locators import Locators

class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.monitors_tab_xpath = Locators.monitors_tab_xpath
        self.apple_monitor_24_linktext = Locators.apple_monitor_24_linktext
    
    def pick_monitor_tab(self):
        #monitors tab
        self.driver.find_element(By.XPATH, Locators.monitors_tab_xpath).click()
    
    def pick_apple_monitor_24(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, Locators.apple_monitor_24_linktext))).click()

