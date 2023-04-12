import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from page_objects.base import Base

class Element_Page(Base):

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    element_text=(By.XPATH,"//div[contains(@class,'header-text')][contains(text(),'Elements')]")
    text_box=(By.XPATH,"//span[normalize-space()='Text Box']")
    check_box=(By.XPATH,"//span[normalize-space()='Check Box']")
    radio_button=(By.XPATH,"//span[normalize-space()='Radio Button']")
    web_tables=(By.XPATH,"//span[normalize-space()='Web Tables']")
    buttons=(By.XPATH,"//span[normalize-space()='Buttons']")
    full_name=(By.XPATH,"//input[@id='userName']")
    user_Email=(By.XPATH,"//input[@id='userEmail']")
    current_address=(By.XPATH,"//textarea[@id='currentAddress']")
    Permanent_address=(By.XPATH,"//textarea[@id='permanentAddress']")
    submit=(By.XPATH,"//button[@id='submit']")
    check_box_text=(By.XPATH,"//span[normalize-space()='Check Box']")
    arrow=(By.XPATH,"//button[@title='Toggle']//*[name()='svg']")
    tick1=(By.XPATH,"//label[@for='tree-node-home']//span[@class='rct-checkbox']")
    tick2=(By.XPATH,"//label[contains(@for,'tree-node-desktop')]//span[contains(@class,'rct-checkbox')]//*[name()='svg']")
    tick3=(By.XPATH,"//label[contains(@for,'tree-node-documents')]//span[contains(@class,'rct-checkbox')]//*[name()='svg']")
    arrow2=(By.XPATH,"//li[@class='rct-node rct-node-parent rct-node-expanded']//li[1]//span[1]//button[1]//*[name()='svg']")
    radio_button_text=(By.XPATH,"//span[normalize-space()='Radio Button']")
    yes_button=(By.XPATH,"//label[@for='yesRadio']")
    Impressive=(By.XPATH,"//label[@for='yesRadio']")


    def check_text_box(self):

        self.click_on_element()
        ele=self.EF.find_element(self.element_text)
        actions=ActionChains(self.driver)
        actions.click(ele)
        # self.driver.execute_script("arguments[0].click();",self.element_text)
        time.sleep(3)
        self.EF.find_element(self.text_box).click()
        self.EF.find_element(self.full_name).send_keys("Ashish khade")
        self.EF.find_element(self.user_Email).send_keys("testmailinator.com")
        self.EF.find_element(self.current_address).send_keys("Mayur Nagar Indore")
        self.EF.find_element(self.Permanent_address).send_keys("Indira Gandhi Ward Multai")
        time.sleep(3)
        button=self.EF.find_element(self.submit)
        actions.move_to_element(button).click(button)

    def check_checkbox(self):
        self.click_on_element()
        ele = self.EF.find_element(self.element_text)
        actions = ActionChains(self.driver)
        actions.click(ele)
        time.sleep(3)
        self.EF.find_element(self.check_box_text).click()
        time.sleep(3)
        self.EF.find_element(self.arrow).click()
        time.sleep(3)
        self.EF.find_element(self.tick1).click()
        time.sleep(3)
        self.EF.find_element(self.tick2).click()
        time.sleep(3)
        self.EF.find_element(self.tick3).click()
        time.sleep(3)
        self.EF.find_element(self.arrow2).click()
        time.sleep(3)
        self.EF.find_element(self.arrow2).click()

    def check_radio_button(self):

        self.click_on_element()
        ele = self.EF.find_element(self.element_text)
        actions = ActionChains(self.driver)
        actions.click(ele)
        time.sleep(2)
        self.EF.find_element(self.radio_button_text).click()
        time.sleep(3)
        self.EF.find_element(self.yes_button).click()
        time.sleep(2)
        self.EF.find_element(self.Impressive).click()















