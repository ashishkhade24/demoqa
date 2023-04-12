from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Elem_Func:

    def __init__(self,driver):
        self.driver=driver

    def find_element(self,locator_tuple):
        try:
            element=WebDriverWait(self.driver,10,poll_frequency=1).until(EC.element_to_be_clickable(locator_tuple))
            return element

        except:
               self.driver.save_screenshot("./testdata/screenshot/element_not_found/unable_to_find_element.png")


    def find_elements(self,locator_tuple):
        try:
            element=WebDriverWait(self.driver,10,poll_frequency=1).until(EC.presence_of_all_elements_located(locator_tuple))
            return element

        except:
               self.driver.save_screenshot("./testdata/screenshot/element_not_found/unable_to_find_element.png")

