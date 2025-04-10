from flask.testing import FlaskClient

def test_home_page(test_app: FlaskClient):
    response = test_app.get('/')
    expected_text = "Embark on a thrilling journey and discover the secrets of the enchanted realm in Adventure Quest, a text-based roleplaying game."
    assert expected_text in response.data.decode("utf-8")
    assert response.status_code == 200
