# Import libraries

import requests # type: ignore
import requests.exceptions # type: ignore
import mypy
from requests.exceptions import MissingSchema,InvalidURL
from bs4 import BeautifulSoup # type: ignore
from flask import Flask, render_template, request # type: ignore



app = Flask(__name__)
app.secret_key = "Hello"

[mypy]
ignore_missing_imports = True

# Home page


@app.route('/')
def index()-> object:
    return render_template('index.html')


# Error pages

#Bad Request 
@app.errorhandler(400) 
#Not Found
@app.errorhandler(404)
#Invalid Url
@app.errorhandler(InvalidURL)
#Missing Schema
@app.errorhandler(MissingSchema)
def handle_bad_request(error)-> object:
    return render_template('error.html')

# Information page


@app.route('/url', methods=['POST'])
def url()-> object:
    url= request.form.get('url')
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
  

    #data variables

    name = soup.select("h1",
                       {"class": "header-touch__AppName-sc-1om5ik5-5 PLRmn"})

    version = soup.select(".drfVqx")

    numbers_of_dowloads = soup.find_all(
        "span", {"class": "mini-stats__Info-sc-188veh1-6 hwoUxO"})

    app_description = soup.find_all(
        "p", {"class": "description__Paragraph-sc-45j1b1-1 daWyZe"})

    release_date = soup.select(".jeuKzx")

    try:
      # List with all app's information
      app_information: dict =  {
            "App's Name ": name[0].getText(),
            "App's Version ": version[0].getText(),
            "Number of Dowloads ": numbers_of_dowloads[0].getText(),
            "Release Date": release_date[0].getText(),
            "App's Description": app_description[0].getText()
      }
      # if the address is valid and it is an aptoide app      
      return render_template('application_information.html',
                              data=app_information)

    except Exception:

      # if the address is valid but does not correspond to an application
      return render_template('misspelled_address.html')
      raise Exception


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
