from flask import Flask, render_template, session, request, url_for, redirect, flash
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from cashmoney import models

posts = []
print(posts)
for i in range(0,10):
    print(i)
    project = {}
    project['title'] = "doggo ipsum"
    #project['img'] = "https://img.buzzfeed.com/buzzfeed-static/static/2017-03/21/7/asset/buzzfeed-prod-fastlane-02/sub-buzz-668-1490096330-22.jpg?downsize=700%3A%2A&output-quality=auto&output-format=auto"
    project['img'] = "https://cdn1.medicalnewstoday.com/content/images/articles/322/322868/golden-retriever-puppy.jpg"
    project['description'] = "Doggo ipsum he made many woofs shoob yapper, you are doing me a frighten. I am bekom fat blep doggo very taste wow boof, I am bekom fat waggy wags clouds ur givin me a spook porgo, heckin angery woofer doing me a frighten you are doin me a concern."
    print(project)
    posts.append(project)
    print(posts)


@app.route("/home")
def hello():
    print ("hello there")
    return render_template("home.html", feed = posts)

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/students")
def students():
    return render_template("students.html")

@app.route("/schools")
def schols():
    return render_template("schools.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
