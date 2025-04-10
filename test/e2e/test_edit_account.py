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
            'User-Name': 'AccountToBeEdited',
            'User-Password': 'Password',
            'User-Email': 'updated@example.com'
        })
        client.post('/Login', data={
            'User-Name': 'AccountToBeEdited',
            'User-Password': 'Password'
        })

        response = client.get('/account')
        assert response.status_code == 200
        data = response.data.decode()
        assert 'AccountToBeEdited' in data
        assert 'updated@example.com' in data

        response = client.get('/update')
        assert response.status_code == 200
        data = response.data.decode()
        assert 'AccountToBeEdited' in data
        assert 'updated@example.com' in data
        with client.session_transaction() as sess:
            assert 'username' in sess
            assert sess['username'] == 'AccountToBeEdited'

        response = client.post('/update', data={
             'username': 'editedUsername',
             'email' : 'edited@email.com'
        })

        assert response.status_code == 302

        response = client.get('/update')
        assert response.status_code == 200
        data = response.data.decode()
        assert 'editedUsername' in data
        assert 'edited@email.com' in data
        with client.session_transaction() as sess:
            assert 'username' in sess
            assert sess['username'] == 'editedUsername'

        