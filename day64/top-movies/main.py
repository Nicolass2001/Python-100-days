from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-movies.db"
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

# EDIT FORM

class RateMovieForm(FlaskForm):
    rating = StringField(label='Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label='Done')

# ADD FORM 

class AddMovieForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField(label='Add Movie')

with app.app_context():
    db.create_all()

    # new_movie = Movie(
    #     title="Phone Booth",
    #     year=2002,
    #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    #     rating=7.3,
    #     ranking=10,
    #     review="My favourite character was the caller.",
    #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    # )
    # db.session.add(new_movie)
    # db.session.commit()

    # second_movie = Movie(
    #     title="Avatar The Way of Water",
    #     year=2022,
    #     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    #     rating=7.3,
    #     ranking=9,
    #     review="I liked the water.",
    #     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    # )
    # db.session.add(second_movie)
    # db.session.commit()

@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars()
    all_movies = list(all_movies) # convert the result to a list
    for movie in all_movies:
        movie.ranking = all_movies.index(movie) + 1
    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get('id')
    movie_to_update = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie_to_update.rating = int(form.rating.data)
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form, movie=movie_to_update)

@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        title = form.title.data
        response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key=78ea5efb98cd714ae57f4d6b8dea6154&query={title}")
        data = response.json()
        return render_template('select.html', movies=data['results'])
    return render_template('add.html', form=form)

@app.route("/select")
def select():
    movie_id = request.args.get('id')
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=78ea5efb98cd714ae57f4d6b8dea6154")
    data = response.json()
    new_movie = Movie(
        title=data['title'],
        year=data['release_date'].split('-')[0],
        description=data['overview'],
        rating=0,
        ranking=0,
        review="",
        img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    db.session.refresh(new_movie)
    return redirect(url_for('edit', id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
