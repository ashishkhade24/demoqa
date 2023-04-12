from page_objects.comftest import setup
from page_objects.element import Element_Page
import pytest


@pytest.mark.usefixtures("setup")
class Test_Element:

    def test_element_pages(self):
        obj=Element_Page(self.driver)
        obj.check_text_box()

    def test_checkbox(self):
        obj=Element_Page(self.driver)
        obj.check_checkbox()

    @pytest.mark.sanity
    def test_radio_button(self):
        obj=Element_Page(self.driver)
        obj.check_radio_button()







