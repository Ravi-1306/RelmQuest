import pytest
from app import app


@pytest.fixture(scope='module')
def test_app():
    test = app.test_client()
    test.application.config['TESTING'] = True
    return test