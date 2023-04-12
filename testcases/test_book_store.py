import pytest
from page_objects.comftest import setup
from page_objects.Book_store_app import Book

@pytest.mark.usefixtures("setup")
class Test_Element:

    def test_login(self):
        object=Book(self.driver)
        object.log_in_signup("Ashish","Khade","Ashu","Ashish@1105","Ashish khade","Ashish@1105")

    @pytest.mark.sanity
    def test_book_store_app(self):
        object=Book(self.driver)
        object.book_store_app()




