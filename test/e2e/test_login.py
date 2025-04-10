import pytest
from app import app, db
from src.models import Account
from flask_bcrypt import Bcrypt
# from werkzeug.security import generate_password_hash, check_password_hash

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            # db.create_all()
            yield client
            db.session.remove()
            # db.drop_all()


def test_login(client):
    # Create a test user
    #new_user = Account('test@example.com', 'testuser', hashed_password)
    client.post('/CreateAccount', data={
        'User-Name': 'testuser',
        'User-Password': 'testpassword',
        'User-Email': 'test@example.com'
    })
    # db.session.add(new_user)
    # db.session.commit()
    
    # Test login with correct credentials
    response = client.post('/Login', data={
        'User-Name': 'testuser',
        'User-Password': 'testpassword'
    }, follow_redirects=True)
    assert b'Account' in response.data 
    
    with client.session_transaction() as sess:
        assert 'username' in sess
        assert sess['username'] == 'testuser'
    
def test_login_invalid_credentials(client):
    # Test login with incorrect credentials
    response = client.post('/Login', data={
        'User-Name': 'nonexistentuser',
        'User-Password': 'wrongpassword'
    }, follow_redirects = True)
    assert b'<input type="text" class="form-control" placeholder="User Name" name="User-Name" id="User-Name" required>' in response.data