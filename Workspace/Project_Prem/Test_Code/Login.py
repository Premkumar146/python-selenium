from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Test_Login:
    
    url = "https://opensource-demo.orangehrmlive.com"
    
    # Constructor for launching the Chrome browser for Python Tests
    def __init__(self):
        self.driver = webdriver.Chrome()   
    
    def test_login(self):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value='username').send_keys('Admin')
        self.driver.find_element(by=By.NAME, value='password').send_keys('admin123')
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        assert self.driver.title == 'OrangeHRM'
        self.driver.close()

test = Test_Login()

test.test_login()