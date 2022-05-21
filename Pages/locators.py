from selenium.webdriver.common.by import By

class Locators():
    #Home page objects
    monitors_tab_xpath = (By.XPATH, "/html/body/div[5]/div/div[1]/div/a[4]")
    apple_monitor_24_linktext = (By.LINK_TEXT, "Apple monitor 24")
    cart_nav = (By.CSS_SELECTOR, "#cartur")

    #Product page Apple monitor 24 objects
    
    monitor_img = (By.XPATH, "/html/body/div[5]/div/div[1]/div/div/div/div/img")
    
    product_name = (By.XPATH, "/html/body/div[5]/div/div[2]/h2")
    
    product_price = (By.XPATH, "/html/body/div[5]/div/div[2]/h3")

    #cart page
    cart_header = (By.TAG_NAME,'h2')
    cart_title_x = (By.XPATH, '//td[contains(text(),\'Apple monitor 24\')]')
    cart_price_x = (By.XPATH,'//td[contains(text(),\'400\')]')
    button_cart = (By.CSS_SELECTOR,'.btn.btn-success')
