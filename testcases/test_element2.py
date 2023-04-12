import pytest
from page_objects.comftest import setup
from page_objects.element2 import Check_Element

@pytest.mark.usefixtures("setup")
class Test_Element:

    def test_buttons(self):
        obj=Check_Element(self.driver)
        obj.check_buttons()

    def test_links(self):
        obj = Check_Element(self.driver)
        obj.check_links()

    def test_broken_images(self):
        obj=Check_Element(self.driver)
        obj.check_broken_links()

    def test_download_upload(self):
        obj = Check_Element(self.driver)
        obj.check_download_and_upload()

    @pytest.mark.sanity
    def test_dynamic_properties(self):
        obj = Check_Element(self.driver)
        obj.check_dynamic_properties()



