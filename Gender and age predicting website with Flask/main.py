from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Enter  /guess/your_name  with URL</h1>"

@app.route('/guess/<name>')
def home(name):

    response_age = requests.get(url=f'https://api.agify.io?name={name}')
    response_age.raise_for_status()
    data_age = response_age.json()
    my_age = data_age['age']
    response_gender = requests.get(url=f'https://api.genderize.io?name={name}')
    response_gender.raise_for_status()
    data_gender = response_gender.json()
    my_gender = data_gender['gender']
    name = name.capitalize()
    return render_template("index.html",na = name,age=my_age,gender=my_gender)


if __name__ == "__main__":
    app.run(debug=True)



