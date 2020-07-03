
import pytest


@pytest.mark.qn
def test_firstProgram(setup):
    print("local invoke onfixture Examp1")


def test_creditCard1(sauna):
    print("Invoke by text in the name Examp1")

@pytest.mark.skip
def test_creditCard3():
    print("Invoke by text in the name Examp1")

@pytest.mark.xfail
def test_second():
    print("xfail the test")
