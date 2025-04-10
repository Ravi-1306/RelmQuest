from flask.testing import FlaskClient
from requests_html import HTMLSession
from bs4 import BeautifulSoup

def test_worldmap_page(test_app: FlaskClient):
    response = test_app.get('/Worldmap')
    expected_text = "Your nation awaits ..."
    assert expected_text in response.data.decode("utf-8")
    assert response.status_code == 200
    data = response.data.decode()
    print(data)

    soup = BeautifulSoup(response.data, 'html.parser')

    button_exists = soup.find(class_='btn')
    assert button_exists is not None

    expected_texts = [
       "Republic of Maz",
       "Drukh Empire",
       "Principality of Ledonia",
       "Grand Duchy of Pildock",
       "Bishopric of Wignia",
       "Republic of Horshedia"
       ]

    button_texts = [button.text.strip() for button in soup.find_all(class_='btn')]   
    assert any(expected_text.strip() for expected_text in expected_texts for button_text in button_texts)


