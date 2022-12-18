from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Test_LoginFailure:
    
    url = "https://opensource-demo.orangehrmlive.com"
    
    # Constructor for launching the Chrome browser for Python Tests
    def __init__(self):
        self.driver = webdriver.Chrome()   

    def test_loginfailure(self):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value='username').send_keys('Admin123')
        self.driver.find_element(by=By.NAME, value='password').send_keys('admin1234')
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        time.sleep(5)
        assert self.driver.find_element(by=By.CLASS_NAME, value='oxd-layout'), 'Login is not successful'
        print('Login is successful')

test = Test_LoginFailure()

test.test_loginfailure()