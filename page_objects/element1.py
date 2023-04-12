from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from page_objects.base import Base
import time

class Element_Page(Base):

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    web_tables_text=(By.XPATH,"//div[contains(@class,'element-list collapse show')]/ul/li[4]")
    webtable=(By.XPATH,"//div[@class='element-list collapse show']//li[@id='item-3']")
    add_button=(By.ID,"addNewRecordButton")
    first_name_text=(By.XPATH,"//input[@id='firstName']")
    last_name_text=(By.XPATH,"//input[@id='lastName']")
    user_email=(By.XPATH,"//input[@id='userEmail']")
    age=(By.XPATH,"//input[@id='age']")
    salary=(By.XPATH,"//input[@id='salary']")
    department=(By.XPATH,"//input[@id='department']")
    submit_button=(By.XPATH,"//button[@id='submit']")
    search_box=(By.XPATH,"//input[@id='searchBox']")
    search_button=(By.ID,"basic-addon2")
    edit_button=(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[7]/div[1]/span[1]/*[name()='svg'][1]")
    delete_button=(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[7]/div[1]/span[2]/*[name()='svg'][1]")
    element_text=(By.XPATH,"//div[contains(@class,'header-text')][contains(text(),'Elements')]")


    def add_user(self):

        self.click_on_element()
        element = self.EF.find_element(self.web_tables_text)
        time.sleep(3)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element)
        actions = ActionChains(self.driver)
        time.sleep(3)
        button=self.EF.find_element(self.add_button)
        actions.click(button).perform()
        time.sleep(2)
        self.EF.find_element(self.first_name_text).send_keys("Ashish")
        time.sleep(3)
        self.EF.find_element(self.last_name_text).send_keys("Khade")
        time.sleep(3)
        self.EF.find_element(self.user_email).send_keys("testas@mailinator.com")
        time.sleep(3)
        self.EF.find_element(self.age).send_keys("27")
        time.sleep(3)
        self.EF.find_element(self.salary).send_keys("10000")
        time.sleep(3)
        self.EF.find_element(self.department).send_keys("quality")
        time.sleep(2)
        self.EF.find_element(self.submit_button).click()

    def search_user(self):
        self.click_on_element()
        element = self.EF.find_element(self.web_tables_text)
        time.sleep(3)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        self.EF.find_element(self.search_box).send_keys("vega")
        time.sleep(3)
        self.EF.find_element(self.search_button).click()

    def edit_user(self):
        self.click_on_element()
        time.sleep(3)
        element=self.EF.find_element(self.web_tables_text)
        time.sleep(3)
        self.driver.execute_script("arguments[0].scrollIntoView();",element)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();",element)
        time.sleep(3)
        self.EF.find_element(self.edit_button).click()
        time.sleep(3)
        name=self.EF.find_element(self.first_name_text)
        time.sleep(3)
        name.send_keys(Keys.CONTROL+"a")
        time.sleep(3)
        name.send_keys("Ashu")
        time.sleep(3)
        lastname=self.EF.find_element(self.last_name_text)
        time.sleep(3)
        lastname.send_keys(Keys.CONTROL+"a")
        time.sleep(3)
        lastname.send_keys("king")
        time.sleep(3)
        self.EF.find_element(self.submit_button).click()
        time.sleep(3)
        self.EF.find_element(self.delete_button).click()
        time.sleep(3)



















