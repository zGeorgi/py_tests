
import pytest

from test.logger_class import open_logger


@pytest.mark.usefixtures("setup")
class Test_Example(open_logger):


    def test_second(self):
        log = self.thi_logger()
        log.info("some exam2 second test")
    @pytest.mark.fil
    def test_fift(self, loading_data):
        log = self.thi_logger()
        log.debug(loading_data)

    @pytest.mark.xfail
    def test_sixt(self):
        print("some exam2 sixt test")

    @pytest.mark.skip
    def test_seven(self):
        print("some exam2 seven test")
