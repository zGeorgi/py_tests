import pytest


@pytest.fixture(scope="class")
def setup():
    print("fixtures code will be executing first")
    yield
    print("'yield' is always execute Last")


@pytest.fixture()
def dataLoad():
    print("Loading a data..")
    return ["georgi", "dimotrov", "someWebpage.com"]

# parametrazation in fixtures
@pytest.fixture(params=[("chrome","georgi"), ("firefox", "dimitrov"), "IE"])
def crossBrowser(request):
    return request.param
