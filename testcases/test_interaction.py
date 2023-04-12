import pytest
from page_objects.comftest import setup
from page_objects.interaction import Interaction

@pytest.mark.usefixtures("setup")
class Test_Interaction:

    def test_sortable(self):
        obj=Interaction(self.driver)
        obj.sortable()

    def test_selectable(self):
        obj=Interaction(self.driver)
        obj.selectable()

    def test_resizable(self):
        object=Interaction(self.driver)
        object.resizable()

    def test_drag_and_drop(self):
        object = Interaction(self.driver)
        object.drag_and_drop()

    @pytest.mark.sanity
    def test_draggable(self):
        object = Interaction(self.driver)
        object.draggable()



