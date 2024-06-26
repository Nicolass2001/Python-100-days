from random import choice
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

API_KEY = "TopSecretAPIKey"
app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def random():
    c = choice(db.session.execute(db.select(Cafe)).scalars().all())
    # json = jsonify(cafe={
    #     "id": c.id,
    #     "name": c.name,
    #     "map_url": c.map_url,
    #     "img_url": c.img_url,
    #     "location": c.location,
    #     "seats": c.seats,
    #     "has_toilet": c.has_toilet,
    #     "has_wifi": c.has_wifi,
    #     "has_sockets": c.has_sockets,
    #     "can_take_calls": c.can_take_calls,
    #     "coffee_price": c.coffee_price
    # })
    json = jsonify(cafe=c.to_dict())
    return json


@app.route("/all")
def all():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    json = jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    return json


@app.route("/search")
def search():
    loc = request.args.get('loc')
    cafes = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars().all()
    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't hace a cafe at that location."}), 404


@app.route("/add", methods=['POST'])
def add():
    if request.args.get("api-key") != API_KEY:
        return jsonify(error={"Not Found": "Sorry that's not allowed. Make sure you have the correct api_key."}), 403
    new_cafe = Cafe(
        name=request.form["name"],
        map_url=request.form["map_url"],
        img_url=request.form["img_url"],
        location=request.form["location"],
        seats=request.form["seats"],
        has_toilet=bool(request.form["has_toilet"]),
        has_wifi=bool(request.form["has_wifi"]),
        has_sockets=bool(request.form["has_sockets"]),
        can_take_calls=bool(request.form["can_take_calls"]),
        coffee_price=request.form["coffee_price"]
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success":"Successfully added the new cafe."})


@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = request.args.get("new_price")
        db.session.commit()
        return jsonify(response={"success":"Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    if request.args.get("api-key") != API_KEY:
        return jsonify(error={"Not Found": "Sorry that's not allowed. Make sure you have the correct api_key."}), 403
    cafe = db.session.get(Cafe, cafe_id)
    if not cafe:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    db.session.delete(cafe)
    db.session.commit()
    return jsonify(response={"success":"Successfully deleted the cafe."})


# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
