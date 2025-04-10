# import pytest
# from app import app 

# @pytest.fixture
# def client():
#     app.config['TESTING'] = True
#     with app.test_client() as client:
#         yield client
        
# def test_feedback_page_route(client):
#     response = client.get("/feedback_page")
#     assert response.status_code == 200
#     assert b"Please fill out the form" in response.data
    
# def test_form_rendering(client):
#     response = client.get("/feedback_page")
#     assert b'<form action="https://formspree.io/f/mrgwwdnk" method="POST">' in response.data
#     assert b'id="accountEmail"' in response.data
#     assert b'id="issueType"' in response.data
#     assert b'id="feedback"' in response.data
    
# def test_form_submission(client):
#     response = client.post("/feedback_page", data={
#         'accountEmail': 'test@example.com',
#         'issueType': 'Suggestion',
#         'feedback': 'Test feedback'
#     })

import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_feedback_page_route(client):
    """
    Test if the feedback page loads correctly.
    """
    response = client.get("/feedback_page")
    assert response.status_code == 200
    assert b"Please fill out the form" in response.data

def test_form_rendering(client):
    """
    Test if the feedback form is rendered correctly on the page.
    """
    response = client.get("/feedback_page")
    assert b'<form action="https://formspree.io/f/mrgwwdnk" method="POST">' in response.data
    assert b'id="accountEmail"' in response.data
    assert b'id="issueType"' in response.data
    assert b'id="feedback"' in response.data



