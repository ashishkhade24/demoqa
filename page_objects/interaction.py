from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from page_objects.base import Base

class Interaction(Base):

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    one= (By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]")
    two= (By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]")
    six= (By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[6]")
    four= (By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[4]")
    grid= (By.XPATH,"//a[@id='demo-tab-grid']")
    one_tab=(By.XPATH,"//div[@class='create-grid']//div[@class='list-group-item list-group-item-action'][normalize-space()='One']")
    nine_tab=(By.XPATH,"//div[normalize-space()='Nine']")
    seven_tab=(By.XPATH,"//div[normalize-space()='Seven']")
    tab_grid=(By.XPATH,"//a[@id='demo-tab-grid']")
    all_grids=(By.XPATH,"//div[@id='gridContainer']/div/li")
    five_tab=(By.XPATH,"//div[@class='create-grid']//div[@class='list-group-item list-group-item-action'][normalize-space()='Five']")
    resize_1= (By.XPATH,"//div[@id='resizableBoxWithRestriction']")
    resize_2= (By.XPATH,"//div[@id='resizable']")
    drag=(By.XPATH,"//div[@id='draggable']")
    drop=(By.XPATH,"//div[@id='simpleDropContainer']//div[@id='droppable']")
    accept=(By.XPATH,"//a[@id='droppableExample-tab-accept']")
    acceptable=(By.XPATH,"//div[@id='acceptable']")
    not_acceptable=(By.XPATH,"//div[@id='notAcceptable']")
    drag2=(By.XPATH,"//div[@id='acceptDropContainer']//div[@id='droppable']")
    prevent_propoagation=(By.XPATH,"//a[@id='droppableExample-tab-preventPropogation']")
    drag_box=(By.XPATH,"//div[@id='dragBox']")
    outer_dropable=(By.XPATH,"//div[@id='notGreedyDropBox']")
    inner=(By.XPATH,"//div[@id='greedyDropBoxInner']")
    revertable=(By.XPATH,"//div[@id='revertable']")
    drop_here=(By.XPATH,"//div[@id='revertableDropContainer']//div[@id='droppable']")
    revert_draggable=(By.XPATH,"//a[@id='droppableExample-tab-revertable']")
    revertable_box=(By.XPATH,"//div[@id='revertable']")
    not_revertable=(By.XPATH,"//div[@id='notRevertable']")
    dropabble_box=(By.XPATH,"//div[@id='revertableDropContainer']//div[@id='droppable']")
    simple_drag=(By.XPATH,"//div[@id='dragBox']")
    axix_restricted=(By.XPATH,"//a[@id='draggableExample-tab-axisRestriction']")
    only_x=(By.XPATH,"//div[@id='restrictedX']")
    only_y=(By.XPATH,"//div[@id='restrictedY']")
    container_restricted=(By.XPATH,"//a[@id='draggableExample-tab-containerRestriction']")
    draggable_ui=(By.XPATH,"//div[@class='draggable ui-widget-content ui-draggable ui-draggable-handle']")
    cursor_style=(By.XPATH,"//a[@id='draggableExample-tab-cursorStyle']")
    center=(By.XPATH,"//div[@id='cursorCenter']")
    top_left=(By.XPATH,"//div[@id='cursorTopLeft']")
    cursor_buttom=(By.XPATH,"//div[@id='cursorBottom']")
    sortable_text = (By.XPATH, "//span[normalize-space()='Sortable']")
    selectable_text=(By.XPATH,"//span[normalize-space()='Selectable']")
    demo_grid=(By.XPATH,"//a[@id='demo-tab-grid']")
    list_item=(By.XPATH,"//ul[@id='verticalListContainer']/li")
    resizable_text=(By.XPATH,"//span[normalize-space()='Resizable']")
    dropable=(By.XPATH,"//span[normalize-space()='Droppable']")
    draggable_text=(By.XPATH,"//span[normalize-space()='Dragabble']")

    def sortable(self):

        self.click_on_interaction()
        element = self.EF.find_element(self.sortable_text)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10, 200).perform()
        time.sleep(3)
        tab1=self.EF.find_element(self.one)
        actions.move_to_element(tab1).click_and_hold().move_by_offset(0,100).release().perform()
        time.sleep(3)
        tab3=self.EF.find_element(self.six)
        actions.move_to_element(tab3).click_and_hold().move_by_offset(0,-300).release().perform()
        time.sleep(3)
        tab2=(self.EF.find_element(self.two))
        actions.move_to_element(tab2).click_and_hold().move_by_offset(0,200).release().perform()
        time.sleep(3)
        self.EF.find_element(self.grid).click()
        time.sleep(3)
        button1=self.EF.find_element(self.one_tab)
        button2 = self.EF.find_element(self.nine_tab)
        actions.drag_and_drop(button1, button2).perform()
        time.sleep(3)
        button3=self.EF.find_element(self.seven_tab)
        button4=self.EF.find_element(self.five_tab)
        actions.drag_and_drop(button3, button4).perform()
        time.sleep(5)

    def selectable(self):

        self.click_on_interaction()
        element = self.EF.find_element(self.selectable_text)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10, 200).perform()
        time.sleep(3)
        items=self.EF.find_elements(self.list_item)
        for x in items:
            x.click()
            time.sleep(1)
        time.sleep(3)
        self.EF.find_element(self.tab_grid).click()
        select_all=self.EF.find_elements(self.all_grids)
        for y in select_all:
            y.click()
            time.sleep(3)

    def resizable(self):
        self.click_on_interaction()
        element = self.EF.find_element(self.resizable_text)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10, 200).perform()
        element=self.EF.find_element(self.resize_1)
        element.size = {'width': 150, 'height': 150}
        time.sleep(3)

    def drag_and_drop(self):
        self.click_on_interaction()
        element = self.EF.find_element(self.dropable)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10, 200).perform()
        drag_ele=self.EF.find_element(self.drag)
        drop_ele=self.EF.find_element(self.drop)
        actions.drag_and_drop(drag_ele,drop_ele).perform()
        time.sleep(3)
        self.EF.find_element(self.accept).click()
        box1=self.EF.find_element(self.acceptable)
        box2=self.EF.find_element(self.not_acceptable)
        box3=self.EF.find_element(self.drag2)
        time.sleep(3)
        actions.drag_and_drop(box1,box3).perform()
        time.sleep(3)
        actions.drag_and_drop(box2,box3).perform()
        time.sleep(2)
        self.EF.find_element(self.prevent_propoagation).click()
        box4=self.EF.find_element(self.drag_box)
        box5=self.EF.find_element(self.outer_dropable)
        box6=self.EF.find_element(self.inner)
        actions.drag_and_drop(box4,box5).perform()
        time.sleep(3)
        actions.scroll_by_amount(10,200).perform()
        time.sleep(2)
        actions.drag_and_drop(box4,box6).perform()
        time.sleep(3)
        self.EF.find_element(self.revert_draggable).click()
        will_revert=self.EF.find_element(self.revertable_box)
        time.sleep(3)
        not_revert=self.EF.find_element(self.not_revertable)
        time.sleep(2)
        drop_box1=self.EF.find_element(self.dropabble_box)
        actions.drag_and_drop(will_revert,drop_box1).perform()
        time.sleep(3)
        actions.drag_and_drop(not_revert,drop_box1).perform()

    def draggable(self):
        self.click_on_interaction()
        element = self.EF.find_element(self.draggable_text)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10, 200).perform()
        box1=self.EF.find_element(self.simple_drag)
        actions=ActionChains(self.driver)
        actions.move_to_element(box1).drag_and_drop_by_offset(box1,100,200).perform()
        time.sleep(2)
        self.EF.find_element(self.axix_restricted).click()
        x_direction=self.EF.find_element(self.only_x)
        actions.move_to_element(x_direction).drag_and_drop_by_offset(x_direction,150,0).perform()
        time.sleep(2)
        y_direction=self.EF.find_element(self.only_y)
        actions.move_to_element(y_direction).drag_and_drop_by_offset(y_direction,0,200).perform()
        time.sleep(3)
        self.EF.find_element(self.container_restricted).click()
        box2=self.EF.find_element(self.draggable_ui)
        actions.move_to_element(box2).drag_and_drop_by_offset(box2,400,100).perform()
        time.sleep(3)
        self.EF.find_element(self.cursor_style).click()
        top_box=self.EF.find_element(self.top_left)
        actions.move_to_element(top_box).drag_and_drop_by_offset(top_box,0,-174).perform()
        center_box=self.EF.find_element(self.center)
        actions.move_to_element(center_box).drag_and_drop_by_offset(center_box,200,0).perform()
        time.sleep(3)
        actions.scroll_by_amount(0,200).perform()
        time.sleep(3)
        bottom_right=self.EF.find_element(self.cursor_buttom)
        actions.move_to_element(bottom_right).drag_and_drop_by_offset(bottom_right,20,-100).perform()
        time.sleep(2)
        






















































