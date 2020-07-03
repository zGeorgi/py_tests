import pytest


def test_First_test():
    msg = "Hello "
    assert msg == "hi ", "The test from second demo is fail!"

@pytest.mark.smok
@pytest.mark.skip
def test_second_Cart():
    msg = "Hello "
    assert msg == "hi ", "The test is fail!"


