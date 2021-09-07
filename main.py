# Import libraries 
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, url_for, redirect, session, request

app = Flask(__name__)
app.secret_key = "Hello"


# Land page

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/url', methods=['POST'])
def url():

    url = request.form.get('url')
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')

    #data variables

    name = soup.select("h1", {"class": "header-touch__AppName-sc-1om5ik5-5 PLRmn"})

    version = soup.select(".drfVqx")

    numbers_of_dowloads = soup.find_all(
        "span", {"class": "mini-stats__Info-sc-188veh1-6 hwoUxO"})

    app_description = soup.find_all(
        "p", {"class": "description__Paragraph-sc-45j1b1-1 daWyZe"})

    release_date = soup.select(".jeuKzx")

    # List with all app's info 

    app_information = {
        "App's Name ": name[0].getText(),
        "App's Version ": version[0].getText(),
        "Number of Dowloads ": numbers_of_dowloads[0].getText(),
        "Release Date": release_date[0].getText(),
        "App's Description": app_description[0].getText()
    }
    return render_template('application_information.html', data=app_information )

 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug = True)