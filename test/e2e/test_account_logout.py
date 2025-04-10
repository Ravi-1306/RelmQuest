from test.utils import clear_db
from src.models import db, Class, Race, Country, Location, Character, Account, Ability, Char_ABLI
from sqlalchemy import select
from app import session, app


def test_logout():
    app.config['TESTING'] = True
    client = app.test_client()

    client.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired@example.com'
        })
    client.post('/Login', data={
        'User-Name': 'LostInHere',
        'User-Password': 'Password'
    })

        # Make a request to the logout route
    response = client.post('/logout', follow_redirects=True)
    assert response.status_code == 200 

        # Assert that the session data is cleared after logout
    with client as c:
        with c.session_transaction() as sess:
            assert 'username' not in sess