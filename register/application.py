from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'super secret'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'lecture.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Registrant(db.Model):
    __tablename__ = 'registrants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Registrant %r>' % self.name


@app.route("/")
def index():
    users = Registrant.query.all()
    return render_template("index.html", users=users)


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template('register.html')
    else:
        name = request.form.get("name")
        email = request.form.get("email")
        if not name or not email:
            return render_template("apology.html", message="You must provide both name and email!")
        registrant = Registrant(name=name, email=email)
        db.session.add(registrant)
        db.session.commit()
        return redirect(url_for('.index'))
