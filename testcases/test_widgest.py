from page_objects.comftest import setup
from page_objects.widgest import Widget
import pytest

@pytest.mark.usefixtures("setup")
class Test_windgest:

    def test_accordian(self):
        obj=Widget(self.driver)
        obj.check_accordian()

    def test_auto_complete(self):
        obj = Widget(self.driver)
        obj.check_auto_complete()

    def test_date_picker(self):
        obj = Widget(self.driver)
        obj.check_date_time()

    def test_slider(self):
        obj = Widget(self.driver)
        obj.check_slider()

    def test_progress_bar(self):
        obj = Widget(self.driver)
        obj.check_progress_bar_and_tabs()

    @pytest.mark.sanity
    def test_select_menu(self):
        obj = Widget(self.driver)
        obj.menu_and_select_menu()









