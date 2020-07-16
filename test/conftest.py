# send multi data, scope,
import pytest


@pytest.fixture()
def setup():
    print("fixture Setup Browser!")
    yield
    print("Yield execute Last!")


@pytest.fixture(params=[("georgi", "dimitrov"), ("firefox", "Mozila"), (23, 56)])
def loading_data(request):
    return request.param
