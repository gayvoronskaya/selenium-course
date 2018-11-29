import pytest

from lesson10.application import Application

@pytest.fixture
def create_page(request):
    app = Application()
    request.addfinalizer(app.quit)
    return app
