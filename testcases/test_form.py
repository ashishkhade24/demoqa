from page_objects.comftest import setup
from page_objects.form import Forms
import pytest

@pytest.mark.usefixtures("setup")
class Test_Form:

    def test_form(self):
        obj=Forms(self.driver)
        obj.check_form()
