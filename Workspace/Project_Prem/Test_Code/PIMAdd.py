from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Test_PIMAdd:
    
    url = "https://opensource-demo.orangehrmlive.com"
    
    # Constructor for launching the Chrome browser for Python Tests
    def __init__(self):
        self.driver = webdriver.Chrome()   
    
    def test_PIMAdd(self):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value='username').send_keys('Admin')
        self.driver.find_element(by=By.NAME, value='password').send_keys('admin123')
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        assert self.driver.title == 'OrangeHRM'
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input').send_keys('Prem')
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input').send_keys('Kumar')
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()
        time.sleep(10)
        print('User has been successfully added to the list')
        self.driver.close()

test = Test_PIMAdd()

test.test_PIMAdd()