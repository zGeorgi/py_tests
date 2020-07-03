import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample2:

    def test_DataLoad(self, dataLoad):
        print(dataLoad)