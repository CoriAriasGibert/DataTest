import pytest

from main import app, url

#we activate the test in the shell by writing pytest


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


# if the homepage work
def test_home(client):
    response = client.get('/')
    assert b'Home page' in response.data


# if the address is valid
def test_valid_url(client):
    response = client.post(
        '/url', data={'url': "https://lords-mobile.fr.aptoide.com/app"})
    assert b"<p><h3> App&#39;s Version  : </h3>  2.61</p>" in response.data


#if it is a misspelled url
def test_invalid_url(client):
    response = client.post('/url', data={'url': "http://tutia.com"})
    assert b'<h1> Misspelled address or is not an aptoide app </h1>' in response.data


#if the url corresponds to an external link


def test_external_url(client):
    response = client.post('/url', data={'url': "https://www.facebook.com/"})
    assert b'<h1> Misspelled address or is not an aptoide app </h1>' in response.data


#if it is not a url


def test_not_url(client):
    response = client.post('/url', data={'url': "hello "})
    assert b'<title>error</title>' in response.data


#if the url doesn't exist


def test_empti_url(client):
    response = client.post('/url', data={'url': " "})
    assert b'<title>error</title>' in response.data
