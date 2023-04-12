from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
from page_objects.base import Base

class Forms(Base):
    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    practice_form=(By.XPATH,"//span[normalize-space()='Practice Form']")
    name=(By.ID,"firstName")
    lastname=(By.ID,"lastName")
    mail=(By.ID,"userEmail")
    radio_button=(By.XPATH,"//div[@id='genterWrapper']/div/div/label")
    male=(By.XPATH,"//label[@for='gender-radio-1']")
    female=(By.XPATH,"//label[@for='gender-radio-2']")
    others=(By.XPATH,"//label[@for='gender-radio-3']")
    number=(By.ID,"userNumber")
    dob=(By.ID,"dateOfBirthInput")
    month=(By.XPATH,"//select[@class='react-datepicker__month-select']")
    year=(By.XPATH,"//select[@class='react-datepicker__year-select']")
    date=(By.XPATH,"//div[@aria-label='Choose Thursday, May 11th, 1995']")
    hobbies=(By.XPATH,"//div[@id='hobbiesWrapper']/div/div")
    upload_picture=(By.ID,"uploadPicture")
    current_address=(By.ID,"currentAddress")
    state=(By.ID,"//div[contains(text(),'Select State')]")
    city=(By.ID,"//div[contains(text(),'Select City')]")
    subject=(By.XPATH,"//input[@id='subjectsInput']")
    listbox=(By.XPATH,"//div[@role='listbox']")
    select_state=(By.ID,"react-select-3-input")
    select_city=(By.ID,"react-select-4-input")
    submit=(By.XPATH,"//button[@id='submit']")

    def check_form(self):
        self.click_on_forms()
        time.sleep(2)
        self.EF.find_element(self.practice_form).click()
        time.sleep(2)
        self.EF.find_element(self.name).send_keys("ashu")
        time.sleep(2)
        self.EF.find_element(self.lastname).send_keys("kumar")
        time.sleep(2)
        self.EF.find_element(self.mail).send_keys("testmailinator.com")
        time.sleep(3)
        buttons=self.EF.find_elements(self.radio_button)
        for button in buttons:
            button.click()
            time.sleep(2)
        time.sleep(1)
        self.EF.find_element(self.number).send_keys("7987111111")
        time.sleep(2)
        actions=ActionChains(self.driver)
        dates=self.EF.find_element(self.dob)
        actions.scroll_by_amount(10,100).perform()
        time.sleep(3)
        actions.move_to_element(dates).click().perform()
        time.sleep(2)
        select_date=Select(self.EF.find_element(self.month))
        time.sleep(3)
        select_date.select_by_visible_text("May")
        time.sleep(2)
        select_year=Select(self.EF.find_element(self.year))
        time.sleep(2)
        select_year.select_by_value("1995")
        time.sleep(1)
        self.EF.find_element(self.listbox)
        time.sleep(1)
        self.EF.find_element(self.date).click()
        time.sleep(2)
        actions.scroll_by_amount(10, 100).perform()
        time.sleep(3)
        self.EF.find_element(self.subject).send_keys("eng")
        time.sleep(3)
        drop_down = self.driver.find_element(By.XPATH, "//*[text()='English']")
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.click(on_element=drop_down)
        time.sleep(2)
        actions.perform()
        time.sleep(2)
        self.EF.find_element(self.subject).send_keys("ch")
        time.sleep(3)
        drop_down1= self.driver.find_element(By.XPATH, "//*[text()='Chemistry']")
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.click(on_element=drop_down1)
        time.sleep(2)
        actions.perform()
        time.sleep(3)
        actions.scroll_by_amount(10, 100).perform()
        hobbies=self.EF.find_elements(self.hobbies)
        for hobby in hobbies:
            hobby.click()
            time.sleep(1)
        actions.scroll_by_amount(10, 100).perform()
        location=r"C://Users/Quick/Downloads/Screenshot.png3"
        image=self.EF.find_element(self.upload_picture)
        time.sleep(60)
        actions.click(on_element=image)
        actions.send_keys(location)
        time.sleep(5)
        actions.scroll_by_amount(10, 100).perform()
        self.EF.find_element(self.current_address).send_keys("Mayur Nagar Pukhraj City Indore")
        time.sleep(2)
        actions.scroll_by_amount(10,200).perform()
        print("before")
        time.sleep(3)
        self.EF.find_element(self.state).click()
        print("scrolled")
        time.sleep(2)
        self.EF.find_element(self.select_state).send_keys("har")
        time.sleep(2)
        option=self.EF.find_element(By.XPATH,"//*[text()='Haryana']")
        time.sleep(3)
        actions.click(on_element=option)
        time.sleep(2)
        self.EF.find_element(self.city).click()
        time.sleep(3)
        self.EF.find_element(self.select_city).send_keys('ag')
        time.sleep(3)
        option1=self.EF.find_element(By.XPATH,"//*[text()='Agra']")
        time.sleep(3)
        actions.click(on_element=option1)
        time.sleep(2)
        self.EF.find_element(self.submit).click()























