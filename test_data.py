import pytest
from flask import Flask, render_template, request


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
    response = client.post('/url', data={'url': "https://lords-mobile.fr.aptoide.com/app"})
    assert b"<p><h3> App&#39;s Version  : </h3>  2.61</p>" in response.data

    


#if it is an external url
def test_invalid_url(client):
  with pytest.raises (Exception):
    raise Exception(response = client.post('/url', data={'url': "https://lordsobilptoide.com/app"}))




#if the url corresponds to an external link

def test_external_url(client):
  with pytest.raises(Exception):
    raise Exception(response = client.post('/url', data={'url': "https://www.facebook.com/"}))
  assert b'misspelled_address'




#if it is not a url

def test_not_url(client):
  response = client.post('/url', data={'url': "hello "})
  assert b'error' in response.data

#if the url doesn't exist

def test_empti_url(client):
  response = client.post('/url', data={'url': " "})
  assert b'error' in response.data

