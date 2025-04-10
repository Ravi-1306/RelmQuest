import pytest
from app import app, db
from src.models import Account

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            # db.create_all()
            yield client
            db.session.remove()
            # db.drop_all()

def test_create_account(client):
    # Test account creation with valid data
    response = client.post('/CreateAccount', data={
        'User-Name': 'testuser',
        'User-Password': 'testpassword',
        'User-Email': 'test@example.com'
    }, follow_redirects=True)

    assert b'<h5>Welcome, testuser</h5>'
    
    # Check if the account was created in the database
    created_user = Account.query.filter_by(username='testuser').first()
    assert created_user is not None

    with client.session_transaction() as sess:
        assert 'username' in sess
        assert sess['username'] == 'testuser'
    
def test_create_account_invalid_data(client):
    # Test account creation with missing data
    response = client.post('/CreateAccount', data={
        'User-Name': '',
        'User-Password': '',
        'User-Email': ''
    })
    assert b'All fields are required.'

def test_create_account_existing_user(client):
    # Create a user first
    new_user = Account('test@example.com', 'testuser', 'hashed_password')
    # db.session.add(new_user)
    # db.session.commit()

    response = client.post('/CreateAccount', data={
        'User-Name': 'testuser',
        'User-Password': 'testpassword',
        'User-Email': 'test@example.com'
    }, follow_redirects=True)
    assert b'Username already exists' in response.data