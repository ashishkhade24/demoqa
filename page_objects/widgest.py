import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from page_objects.base import Base
from selenium.webdriver.support.select import Select

class Widget(Base):

    def __int__(self,driver):
        self.driver=driver
        super().__init__(driver)

    accordian=(By.XPATH,"//span[normalize-space()='Accordian']")
    first_heading=(By.ID,"section1Heading")
    second_heading=(By.ID,"section2Heading")
    third_heading=(By.ID,"section3Heading")
    auto_complete=(By.XPATH,"//span[normalize-space()='Auto Complete']")
    auto_complete_text=(By.ID,"autoCompleteMultipleInput")
    auto_complete_text1=(By.ID,"autoCompleteSingleInput")
    date_picker=(By.XPATH,"//span[normalize-space()='Date Picker']")
    date_input=(By.XPATH,"//input[@id='datePickerMonthYearInput']")
    month=(By.XPATH,"//select[@class='react-datepicker__month-select']")
    year=(By.XPATH,"//select[@class='react-datepicker__year-select']")
    list_box=(By.XPATH,"//div[@role='listbox']")
    select_date=(By.XPATH,"//div[@aria-label='Choose Saturday, June 26th, 2010']")
    date_time_picker=(By.XPATH,"//div[@id='dateAndTimePicker']//div[@class='react-datepicker-wrapper']")
    month_select=(By.XPATH,"//span[contains(@class,'react-datepicker__month-read-view--down-arrow')]")
    month_picker_dropdown=(By.XPATH,"//span[contains(@class,'react-datepicker__month-read-view--selected-month')]")
    list_of_months=(By.XPATH,"//div[@class='react-datepicker__month-dropdown']")
    august_month=(By.XPATH,"//div[@class='react-datepicker__month-option'][normalize-space()='August']")
    dropdown_arrow=(By.XPATH,"//div[@class='react-datepicker__year-read-view']")
    year22=(By.XPATH,"//div[@class='react-datepicker__year-dropdown']//div[8]")
    date_list_box=(By.XPATH,"//div[@role='listbox']")
    aug7=(By.XPATH,"//div[@aria-label='Choose Sunday, August 7th, 2022']")
    time_list=(By.XPATH,"//div[@class='react-datepicker__time']")
    time_selection=(By.XPATH,"//div[@class='react-datepicker__time']//li[20]")
    slider=(By.XPATH,"//span[normalize-space()='Slider']")
    range=(By.XPATH,"//input[contains(@type,'range')]")
    progress_bar=(By.XPATH,"//span[normalize-space()='Progress Bar']")
    star_button=(By.XPATH,"//button[@id='startStopButton']")
    tabs=(By.XPATH,"//span[normalize-space()='Tabs']")
    origin=(By.XPATH,"//a[@id='demo-tab-origin']")
    use=(By.XPATH,"//a[@id='demo-tab-use']")
    tool_tip=(By.XPATH,"//span[normalize-space()='Tool Tips']")
    tool_tip_button1=(By.XPATH,"//button[@id='toolTipButton']")
    tool_tip_text=(By.XPATH,"//input[@id='toolTipTextField']")
    tool_tip_text2=(By.XPATH,"//a[normalize-space()='Contrary']")
    menu=(By.XPATH,"//span[normalize-space()='Menu']")
    select_menu=(By.XPATH,"//span[normalize-space()='Select Menu']")
    main_item=(By.XPATH,"//a[normalize-space()='Main Item 2']")
    main_item1=(By.XPATH,"//a[normalize-space()='Main Item 3']")
    select_option=(By.XPATH,"//div[contains(text(),'Select Option')]")
    select_title=(By.XPATH,"//div[contains(text(),'Select Title')]")
    select_old_style=(By.XPATH,"//select[@id='oldSelectMenu']")
    select=(By.XPATH,"//div[contains(text(),'Select...')]")
    cars=(By.XPATH,"//select[@id='cars']")

    def check_accordian(self):

        self.click_on_widgets()
        time.sleep(3)
        element = self.EF.find_element(self.accordian)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(10,100).perform()
        time.sleep(1)
        self.EF.find_element(self.first_heading).click()
        time.sleep(2)
        actions.scroll_by_amount(10,100).perform()
        time.sleep(1)
        self.EF.find_element(self.second_heading).click()
        time.sleep(3)
        actions.scroll_by_amount(10,300).perform()
        time.sleep(1)
        self.EF.find_element(self.third_heading).click()
        time.sleep(2)
        self.EF.find_element(self.third_heading).click()

    def check_auto_complete(self):
        self.click_on_widgets()
        time.sleep(3)
        element = self.EF.find_element(self.auto_complete)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        self.EF.find_element(self.auto_complete_text).send_keys("Re")
        time.sleep(5)
        element=self.driver.find_element(By.XPATH,"//*[text()='Red']")
        actions=ActionChains(self.driver)
        time.sleep(3)
        actions.click(on_element=element)
        time.sleep(3)
        actions.perform()
        self.EF.find_element(self.auto_complete_text).send_keys("blu")
        time.sleep(3)
        element1=self.driver.find_element(By.XPATH, "//*[text()='Blue']")
        actions = ActionChains(self.driver)
        actions.click(on_element=element1)
        time.sleep(3)
        actions.perform()
        self.EF.find_element(self.auto_complete_text).send_keys("gr")
        time.sleep(3)
        element2=self.driver.find_element(By.XPATH, "//*[text()='Green']")
        time.sleep(2)
        actions.click(on_element=element2)
        time.sleep(2)
        actions.perform()
        actions.scroll_by_amount(10,200).perform()
        time.sleep(2)
        self.EF.find_element(self.auto_complete_text1).send_keys("gre")
        time.sleep(3)
        element4=self.driver.find_element(By.XPATH,"//*[text(),'Green']")
        time.sleep(3)
        actions.click(on_element=element4).perform()
        time.sleep(2)

    def check_date_time(self):
        self.click_on_widgets()
        time.sleep(3)
        element = self.EF.find_element(self.date_picker)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        self.EF.find_element(self.date_input).click()
        time.sleep(2)
        month_selector=Select(self.EF.find_element(self.month))
        time.sleep(2)
        month_selector.select_by_visible_text("June")
        time.sleep(2)
        year_selctor=Select(self.EF.find_element(self.year))
        time.sleep(2)
        year_selctor.select_by_value("2010")
        time.sleep(2)
        self.EF.find_element(self.list_box)
        time.sleep(2)
        self.EF.find_element(self.select_date)
        time.sleep(2)
        option=self.EF.find_element(self.date_time_picker)
        time.sleep(3)
        actions=ActionChains(self.driver)
        actions.move_to_element(option).click().perform()
        time.sleep(3)
        self.EF.find_element(self.month_select).click()
        time.sleep(2)
        month_option=self.EF.find_element(self.list_of_months)
        time.sleep(3)
        actions.move_to_element(month_option).perform()
        time.sleep(3)
        element1=self.EF.find_element(self.august_month)
        time.sleep(3)
        actions.move_to_element(element1).click().perform()
        time.sleep(2)
        self.EF.find_element(self.dropdown_arrow).click()
        time.sleep(2)
        self.EF.find_element(self.year22).click()
        time.sleep(2)
        self.EF.find_element(self.date_list_box)
        time.sleep(2)
        self.EF.find_element(self.aug7).click()
        time.sleep(2)
        element2=self.EF.find_element(self.time_list)
        actions.move_to_element(element2).perform()
        time.sleep(2)
        self.EF.find_element(self.time_selection).click()

    def check_slider(self):
        self.click_on_widgets()
        time.sleep(3)
        element = self.EF.find_element(self.slider)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        slider_arrow=self.EF.find_element(self.range)
        time.sleep(3)
        move = ActionChains(self.driver)
        time.sleep(3)
        move.click_and_hold(slider_arrow).move_by_offset(40, 0).release().perform()
        time.sleep(3)

    def check_progress_bar_and_tabs(self):
        self.click_on_widgets()
        time.sleep(3)
        element = self.EF.find_element(self.progress_bar)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        self.EF.find_element(self.star_button).click()
        time.sleep(3)
        self.EF.find_element(self.star_button).click()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)
        element1= self.EF.find_element(self.tabs)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element1)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element1)
        time.sleep(3)
        self.EF.find_element(self.origin).click()
        time.sleep(2)
        self.EF.find_element(self.use).click()
        time.sleep(2)
        self.driver.back()
        time.sleep(3)
        element2 = self.EF.find_element(self.tool_tip)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element2)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element2)
        time.sleep(3)
        button=self.EF.find_element(self.tool_tip_button1)
        actions=ActionChains(self.driver)
        actions.move_to_element(button).perform()
        time.sleep(2)
        text_field=self.EF.find_element(self.tool_tip_text)
        actions.move_to_element(text_field).click().send_keys("ask").perform()
        time.sleep(3)
        actions.scroll_by_amount(0,100).perform()
        time.sleep(2)
        text=self.EF.find_element(self.tool_tip_text2)
        actions.move_to_element(text).perform()
        time.sleep(3)

    def menu_and_select_menu(self):
        self.click_on_widgets()
        time.sleep(3)
        element = self.EF.find_element(self.menu)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        self.driver.back()
        time.sleep(3)
        element1 = self.EF.find_element(self.select_menu)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element1)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element1)
        time.sleep(3)
        self.EF.find_element(self.select_option).click()
        time.sleep(3)
        option1=self.driver.find_element(By.XPATH,"//div[contains(text(),'Group 1, option 2')]")
        time.sleep(5)
        actions=ActionChains(self.driver)
        actions.click(on_element=option1).perform()
        time.sleep(3)
        self.EF.find_element(self.select_title).click()
        time.sleep(3)
        option2 = self.driver.find_element(By.XPATH, "//div[contains(text(),'Mr.')]")
        actions.click(on_element=option2).perform()
        time.sleep(2)
        old_style=Select(self.EF.find_element(self.select_old_style))
        old_style.select_by_index(1)
        time.sleep(3)
        old_style.select_by_index(2)
        time.sleep(3)
        cars=Select(self.EF.find_element(self.cars))
        cars.select_by_visible_text("Volvo")
        time.sleep(3)
        cars.select_by_visible_text("Saab")















































