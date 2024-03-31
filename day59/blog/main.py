from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get(url="https://api.npoint.io/b906012b88d274de1e1b")
    response.raise_for_status()
    data = response.json()
    return render_template("index.html", posts=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<id>")
def post(id):
    response = requests.get(url="https://api.npoint.io/b906012b88d274de1e1b")
    response.raise_for_status()
    data = response.json()
    post = [post for post in data if int(id) == post['id']][0]
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)