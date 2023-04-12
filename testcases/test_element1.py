import pytest

from page_objects.comftest import setup
from page_objects.element1 import Element_Page

@pytest.mark.usefixtures("setup")
class Test_Element:

    def test_add_user(self):
        obj=Element_Page(self.driver)
        obj.add_user()

    def test_search_user(self):
        obj=Element_Page(self.driver)
        obj.search_user()

    @pytest.mark.sanity
    def test_edit_user(self):
        obj = Element_Page(self.driver)
        obj.edit_user()

