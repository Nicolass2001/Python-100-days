from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user, user_logged_in

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['UPLOAD_FOLDER'] = 'static/files'
login_manager = LoginManager()
login_manager.init_app(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
 
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    user = db.get_or_404(User, int(user_id))
    return user


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    user_name = request.form["name"]
    password = request.form["password"]
    email = request.form["email"]
    hashed_password = generate_password_hash(password=password, method="pbkdf2", salt_length=8)
    new_user = User(
        email=email,
        password=hashed_password,
        name=user_name
    )
    db.session.add(new_user)
    try:
        db.session.commit()
    except:
        flash("Email repeated.")
        return redirect(url_for("register"))
    login_user(new_user)
    return redirect(url_for("secrets"))


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    password = request.form["password"]
    email = request.form["email"]
    user = db.session.execute(db.select(User).where(User.email == email)).scalar()
    if not user:
        flash("Email doesn't exist on the DB.")
        return redirect(url_for("login"))
    if not check_password_hash(user.password, password):
        flash("Wrong password. Idiot.")
        return redirect(url_for("login"))
    login_user(user)    
    return redirect(url_for("secrets"))


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=current_user.is_authenticated)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
@login_required
def download():
    return send_from_directory(app.config['UPLOAD_FOLDER'], "cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
