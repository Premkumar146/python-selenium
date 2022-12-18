from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Test_PIMDelete:
    
    url = "https://opensource-demo.orangehrmlive.com"
    
    # Constructor for launching the Chrome browser for Python Tests
    def __init__(self):
        self.driver = webdriver.Chrome()   
    
    def test_PIMDelete(self):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value='username').send_keys('Admin')
        self.driver.find_element(by=By.NAME, value='password').send_keys('admin123')
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        assert self.driver.title == 'OrangeHRM'
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys('Prem Kumar')
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
        time.sleep(10)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[1]').click()
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]').click()
        time.sleep(5)
        print('User has been deleted successfully')
        self.driver.close()

test = Test_PIMDelete()

test.test_PIMDelete()