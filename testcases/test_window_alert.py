from page_objects.comftest import setup
from page_objects.windows_alert_frame import Window_Alert
import pytest

@pytest.mark.usefixtures("setup")
class Test_windows_and_alert:

    def test_windows_switch(self):
        obj=Window_Alert(self.driver)
        obj.check_windows()

    def test_alert_check(self):
        obj = Window_Alert(self.driver)
        obj.check_alert()

    def test_iframe(self):
        obj = Window_Alert(self.driver)
        obj.check_iframe()

    def test_nested_iframe(self):
        obj = Window_Alert(self.driver)
        obj.check_nested_iframe()

    def test_modal_dialogue(self):
        object=Window_Alert(self.driver)
        object.check_modal_dialogs()



