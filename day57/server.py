from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/guess/<name>")
def guess(name:str):
    name = name.title()
    parameters = {
        "name": name,
    }
    agify_response = requests.get(url="https://api.agify.io", params=parameters)
    agify_response.raise_for_status()
    age = agify_response.json()["age"]
    print(age)
    genderize_response = requests.get(url="https://api.genderize.io", params=parameters)
    genderize_response.raise_for_status()
    gender = genderize_response.json()["gender"]
    print(gender)
    return render_template("guess.html", name=name, gender=gender, age=age)


@app.route("/blog")
def blog():
    blog_response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    blog_response.raise_for_status()
    blog_data = blog_response.json()
    return render_template("blog.html", param=blog_data)

if __name__ == "__main__":
    app.run(debug=True)