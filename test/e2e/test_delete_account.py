import pytest
from app import app, db, session
from src.models import Account
from test.utils import clear_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client
            db.session.remove()

def test_delete_account(client):
        clear_db()
        response = client.post('/CreateAccount', data={
            'User-Name': 'AccountToBeDeleted',
            'User-Password': 'Password',
            'User-Email': 'deleted@example.com'
        })
        client.post('/Login', data={
            'User-Name': 'AccountToBeDeleted',
            'User-Password': 'Password'
        })

        response = client.get('/account')
        assert response.status_code == 200
        data = response.data.decode()
        assert 'AccountToBeDeleted' in data

        with client.session_transaction() as sess:
            assert 'username' in sess
            assert sess['username'] == 'AccountToBeDeleted'
        

        response = client.get('/delete')
        assert response.status_code == 302
        data = response.data.decode()
        assert response.headers['Location'] == '/'