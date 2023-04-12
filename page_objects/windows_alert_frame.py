import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from page_objects.base import Base

class Window_Alert(Base):
    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    browser_window=(By.XPATH,"//span[normalize-space()='Browser Windows']")
    tab_button=(By.XPATH,"//button[@id='tabButton']")
    window_button=(By.XPATH,"//button[@id='windowButton']")
    message_button=(By.XPATH,"//button[@id='messageWindowButton']")
    alert_text=(By.XPATH,"//span[normalize-space()='Alerts']")
    first_button=(By.XPATH,"//button[@id='alertButton']")
    second_button=(By.XPATH,"//button[@id='timerAlertButton']")
    third_button=(By.XPATH,"//button[@id='confirmButton']")
    fourth_button=(By.XPATH,"//button[@id='promtButton']")
    frame_text=(By.XPATH,"//span[normalize-space()='Frames']")
    nested_frames=(By.XPATH,"//span[normalize-space()='Nested Frames']")
    modal=(By.XPATH,"//span[contains(text(),'Modal Dialogs')]")
    small_modal=(By.ID,"showSmallModal")
    large_model=(By.XPATH,"showLargeModal")
    close_large_modal=(By.XPATH,"//button[@id='closeLargeModal']")
    close_small_modal=(By.XPATH,"//span[@aria-hidden='true']")

    def check_windows(self):
        self.click_on_alerts()
        time.sleep(3)
        element=self.EF.find_element(self.browser_window)
        time.sleep(3)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        self.EF.find_element(self.tab_button).click()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0])
        print(self.driver.window_handles)
        time.sleep(3)
        self.EF.find_element(self.window_button).click()
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(3)
        self.EF.find_element(self.message_button).click()
        self.driver.switch_to.window(self.driver.window_handles[3])
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(3)

    def check_alert(self):
        self.click_on_alerts()
        time.sleep(3)
        element=self.EF.find_element(self.alert_text)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        self.EF.find_element(self.first_button).click()
        alert1=self.driver.switch_to.alert
        time.sleep(1)
        alert1.accept()
        time.sleep(3)
        self.EF.find_element(self.second_button).click()
        time.sleep(6)
        alert2=self.driver.switch_to.alert
        time.sleep(1)
        alert2.accept()
        time.sleep(2)
        self.EF.find_element(self.third_button).click()
        time.sleep(2)
        alert3=self.driver.switch_to.alert
        alert3.dismiss()
        time.sleep(2)
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(10,100).perform()
        time.sleep(3)
        self.EF.find_element(self.fourth_button).click()
        time.sleep(2)
        alert4=self.driver.switch_to.alert
        time.sleep(3)
        alert4.send_keys("Ashish")
        time.sleep(2)
        alert4.accept()
        time.sleep(2)

    def check_iframe(self):
        self.click_on_alerts()
        time.sleep(3)
        element = self.EF.find_element(self.frame_text)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        self.driver.switch_to.frame("frame1")
        time.sleep(3)
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.driver.switch_to.frame("frame2")
        time.sleep(2)

    def check_nested_iframe(self):
        self.click_on_alerts()
        time.sleep(3)
        element = self.EF.find_element(self.nested_frames)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(10,300).perform()
        time.sleep(2)
        self.driver.switch_to.frame("frame1")
        time.sleep(3)
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.driver.switch_to.frame(1)
        time.sleep(2)

    def check_modal_dialogs(self):
        self.click_on_alerts()
        element = self.EF.find_element(self.modal)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        self.EF.find_element(self.modal).click()
        time.sleep(2)
        print("clicked")
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10, 100).perform()
        time.sleep(2)
        self.EF.find_element(self.small_modal).click()
        time.sleep(2)
        print("not_clicked")
        self.EF.find_element(self.close_small_modal).click()
        time.sleep(3)
        self.EF.find_element(self.large_model).click()
        time.sleep(3)
        self.EF.find_element(self.large_model).click()
        time.sleep(3)
        self.EF.find_element(self.close_large_modal)
































