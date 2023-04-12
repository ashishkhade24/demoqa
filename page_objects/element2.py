from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from page_objects.base import Base

class Check_Element(Base):

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    buttons=(By.XPATH,"//span[normalize-space()='Buttons']")
    links=(By.XPATH,"//span[normalize-space()='Links']")
    broken_images=(By.XPATH,"//span[normalize-space()='Broken Links - Images']")
    upload_and_download=(By.XPATH,"//span[normalize-space()='Upload and Download']")
    dynamic=(By.XPATH,"//span[normalize-space()='Dynamic Properties']")
    double_click=(By.XPATH,"//button[@id='doubleClickBtn']")
    right_click=(By.XPATH,"//button[@id='rightClickBtn']")
    click=(By.XPATH,"//button[@id='D0KHN']")
    link_home=(By.XPATH,"//a[@id='simpleLink']")
    link_home_page=(By.XPATH,"//a[@id='dynamicLink']")
    valid_link=(By.XPATH,"//a[normalize-space()='Click Here for Valid Link']")
    broken_link=(By.XPATH,"//a[normalize-space()='Click Here for Broken Link']")
    download_button=(By.XPATH,"//a[@id='downloadButton']")
    upload_file=(By.ID,"uploadFile")
    enable_button=(By.XPATH,"//button[@id='enableAfter']")
    visible_after=(By.XPATH,"//button[@id='visibleAfter']")

    def check_buttons(self):
        self.click_on_element()
        time.sleep(3)
        element=self.EF.find_element(self.buttons)
        time.sleep(1)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        actions=ActionChains(self.driver)
        button=self.EF.find_element(self.double_click)
        time.sleep(1)
        actions.double_click(button).perform()
        time.sleep(1)
        button1=self.EF.find_element(self.right_click)
        time.sleep(1)
        actions.context_click(button1).perform()
        time.sleep(1)
        button2=self.EF.find_element(self.click)
        time.sleep(1)
        actions.click(button2).perform()

    def check_links(self):
        self.click_on_element()
        time.sleep(3)
        element = self.EF.find_element(self.links)
        time.sleep(1)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        self.EF.find_element(self.link_home).click()
        time.sleep(1)
        # window_handles[1] is a second window
        self.driver.switch_to.window(self.driver.window_handles[1])
        # prints the title of the second window
        print("Second window title = " + self.driver.title)
        # window_handles[0] is a first window
        self.driver.switch_to.window(self.driver.window_handles[0])
        # prints windows id
        print(self.driver.window_handles)
        time.sleep(1)
        self.EF.find_element(self.link_home_page).click()
        time.sleep(1)
        self.driver.quit()

    def check_broken_links(self):
        self.click_on_element()
        time.sleep(3)
        element = self.EF.find_element(self.broken_images)
        time.sleep(1)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        ele=self.EF.find_element(self.broken_link)
        time.sleep(1)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", ele)
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.EF.find_element(self.valid_link).click()
        self.driver.back()
        print(self.driver.window_handles)

    def check_download_and_upload(self):
        self.click_on_element()
        time.sleep(3)
        element = self.EF.find_element(self.upload_and_download)
        time.sleep(1)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        self.EF.find_element(self.download_button).click()
        time.sleep(3)
        actions = ActionChains(self.driver)
        location= r"C://Users/Quick/Downloads/Screenshot.png3"
        time.sleep(5)
        image=self.EF.find_element(self.upload_file)
        time.sleep(60)
        actions.click(on_element=image)
        actions.send_keys(location)
        time.sleep(60)

    def check_dynamic_properties(self):
        self.click_on_element()
        time.sleep(3)
        element = self.EF.find_element(self.dynamic)
        time.sleep(1)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", element)
        button_check=self.EF.find_element(self.enable_button)
        test=button_check.is_enabled()
        print(test)
        time.sleep(10)
        display=self.EF.find_element(self.visible_after)
        time.sleep(3)
        test1=display.isDisplayed()
        print(test1)


















