import pytest


@pytest.fixture(scope="class")
def setup():
    print("Invoke setup fixture")
    yield
    print("Setup fixture invoke after the test")


@pytest.fixture(params=[("one","five"), ("seven", "tree"), ("four","ten"), ])
def stream_data(request):
    return request.param

@pytest.fixture()
def sauna():
    print("ganz normal sauna club")