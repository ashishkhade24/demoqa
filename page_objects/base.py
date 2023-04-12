from selenium.webdriver.common.by import By
from utility.elementry_function import Elem_Func
import time

class Base:
    def __init__(self,driver):
        self.driver=driver
        self.EF=Elem_Func(driver)

    element1=(By.XPATH,"//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]")
    element=(By.XPATH,"//body/div[@id='app']/div[@class='body-height']/div[@class='home-content']/div[@class='home-body']/div[@class='category-cards']/div[1]")
    forms=(By.XPATH,"//body/div[@id='app']/div[@class='body-height']/div[@class='home-content']/div[@class='home-body']/div[@class='category-cards']/div[2]")
    Alerts=(By.XPATH,"//body/div[@id='app']/div[@class='body-height']/div[@class='home-content']/div[@class='home-body']/div[@class='category-cards']/div[3]")
    widgets=(By.XPATH,"//body/div[@id='app']/div[@class='body-height']/div[@class='home-content']/div[@class='home-body']/div[@class='category-cards']/div[4]")
    interactions=(By.XPATH,"//h5[normalize-space()='Interactions']")
    book_store=(By.XPATH,"//h5[normalize-space()='Book Store Application']")

    def click_on_element(self):
        self.EF.find_element(self.element).click()

    def click_on_forms(self):
        ele=self.EF.find_element(self.forms)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", ele)

    def click_on_alerts(self):
        ele1=self.EF.find_element(self.Alerts)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele1)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", ele1)

    def click_on_widgets(self):
        ele1 = self.EF.find_element(self.widgets)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele1)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", ele1)

    def click_on_interaction(self):
        ele1 = self.EF.find_element(self.interactions)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele1)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", ele1)

    def click_on_book_store(self):
        element=self.EF.find_element(self.book_store)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element)





