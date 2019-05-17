
from flask import Flask, render_template, session, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    userType = db.Column(db.String(80), nullable=False)
    paypal = db.Column(db.String(120), nullable=False)
    verified = db.Column(db.Integer, nullable=False)
    sID = db.Column(db.String(120), nullable=False)
    pic = db.Column(db.String(120), nullable=False)
    projects = db.relationship('Projects', backref = 'user', lazy = True)
    ##Lazy loading refers to objects are returned from a
    ##query without the related objects loaded at first.


    def __repr__(self):
        return '<User %r>' % self.username

class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    userID = db.Column(db.Integer, primary_key=True)
    goal = db.Column(db.Integer, nullable=False)
    current = db.Column(db.Integer, nullable=False)
    projectID = db.Column(db.Integer, nullable = False)
    sID = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/")
def hello():
    print ("hello there")
    return render_template("home.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
