import pytest


@pytest.mark.smok
def test_First_test_Cart():
    print("Hello py")


@pytest.mark.xfail
def test_Great():
    print("Hello ")


def test_crossBrowser(crossBrowser):
    print(crossBrowser)
