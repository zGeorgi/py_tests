import pytest

@pytest.mark.usefixtures("setup")
class TestFixture:

    def test_fixtures_(self):
        print("In fixtures demo method")

    def test_fixt(self):
        print("In fixtures demo method")

    def test_fixt1(self):
        print("In fixtures demo method")