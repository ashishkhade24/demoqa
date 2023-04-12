import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from page_objects.base import Base


class Book(Base):
    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    new_user=(By.XPATH,"//button[@id='newUser']")
    first_name=(By.XPATH,"//input[@id='firstname']")
    last_name=(By.XPATH,"//input[@id='lastname']")
    user_name=(By.XPATH,"//input[@id='userName']")
    password=(By.XPATH,"//input[@id='password']")
    register=(By.XPATH,"//button[@id='register']")
    login=(By.XPATH,"//span[normalize-space()='Login']")
    iframe=(By.TAG_NAME,"iframe")
    checkbox=(By.XPATH,"//iframe[@title='reCAPTCHA']")
    back_button=(By.XPATH,"//button[@id='gotologin']")
    login_user=(By.XPATH,"//input[@id='userName']")
    password_field=(By.XPATH,"//input[@id='password']")
    log_in=(By.XPATH,"//button[@id='login']")
    Book_store=(By.XPATH,"//span[normalize-space()='Book Store']")
    title=(By.XPATH,"//div[contains(text(),'Title')]")
    Author=(By.XPATH,"//div[contains(text(),'Author')]")
    publisher=(By.XPATH,"//div[contains(text(),'Publisher')]")
    git_pocket_guide=(By.XPATH,"//a[normalize-space()='Git Pocket Guide']")
    back_store=(By.XPATH,"//button[@id='addNewRecordButton']")

    def log_in_signup(self,firstname,lastname,Username,Password,user_field,login_password):

        self.click_on_book_store()
        element=self.EF.find_element(self.login)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10, 200).perform()
        self.EF.find_element(self.new_user).click()
        time.sleep(3)
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(10,200).perform()
        time.sleep(3)
        self.EF.find_element(self.first_name).send_keys(firstname)
        self.EF.find_element(self.last_name).send_keys(lastname)
        self.EF.find_element(self.user_name).send_keys(Username)
        self.EF.find_element(self.password).send_keys(Password)
        actions.scroll_by_amount(10, 200).perform()
        time.sleep(3)
        self.EF.find_element(self.back_button).click()
        self.EF.find_element(self.login_user).send_keys(user_field)
        self.EF.find_element(self.password_field).send_keys(login_password)
        time.sleep(3)
        actions.scroll_by_amount(10, 200).perform()
        time.sleep(3)
        self.EF.find_element(self.log_in).click()

    def book_store_app(self):
            self.click_on_book_store()
            element = self.EF.find_element(self.Book_store)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(3)
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(3)
            self.EF.find_element(self.git_pocket_guide).click()
            time.sleep(3)
            actions=ActionChains(self.driver)
            actions.scroll_by_amount(10,350).perform()
            self.EF.find_element(self.back_store).click()





















