from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)

@app.route('/')
def home():
    blog_response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    blog_response.raise_for_status()
    blog_data = blog_response.json()
    return render_template("index.html", blogs=blog_data)


@app.route('/post/<id>')
def post(id):
    blog_response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    blog_response.raise_for_status()
    blog_data = blog_response.json()
    blog = [blog for blog in blog_data if int(id) == blog['id']][0]
    return render_template("post.html", blog=blog)


if __name__ == "__main__":
    app.run(debug=True)
