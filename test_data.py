import pytest
from flask import Flask, render_template, request


from main import url


#we activate the test in the shell by writing pytest

# if the address is valid
def test_valid_url()-> object:
    url=="https://lords-mobile.fr.aptoide.com/app"


#if it is an external url 

def test_invalid_url()-> object:
    with pytest.raises(Exception):
        url("https://lormobe.aptoide.com/app")
        return render_template('misspelled_address.html')

#if the url corresponds to an external link 

def test_external_url ()-> object:
    with pytest.raises(Exception):
        url("https://www.facebook.com/")
        return render_template('misspelled_address.html')


#if it is not a url

def test_not_url()-> object:
    with pytest.raises(Exception):
        url("hello")
        return render_template('error.html')

#if the url doesn't exist

def test_empti_url()-> object:
    with pytest.raises(Exception):
        url(" ")
        return render_template('error.html')

