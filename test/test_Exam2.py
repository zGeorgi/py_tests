import pytest

from test.LoggerClass import LoggerObj


@pytest.mark.usefixtures("setup")
class TestExamp(LoggerObj):

    def test_creditCard1(self, stream_data):
        log = self.getLogger()
        log.info(stream_data)


    @pytest.mark.qn
    def test_creditCard5(self):
        log = self.getLogger()
        log.info("Info from creditCard5")
