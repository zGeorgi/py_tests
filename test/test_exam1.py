
import pytest


@pytest.mark.fil
def test_first():
    print("some exam1 first test")


def test_second():
    print("some exam1 scond test")

pytest.mark.xfail
def test_third():
    print("some exam1 third test")

pytest.mark.skip
def test_fourt():
    print("some exam1 fourt test")
