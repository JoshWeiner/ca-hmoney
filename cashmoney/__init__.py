import sys
from flask import Flask, current_app
from threading import Thread
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import current_app
#from wtf_tinymce import wtf_tinymce
#import setup
#print(package.config)
from time import sleep
import datetime
import os
from datetime import datetime
import urllib  # for urlopen, urlretrieve
import os      # for chdir, makedirs, path.exists
from flask import render_template, flash, redirect, url_for, request, current_app, abort, jsonify, request
from jinja2 import TemplateNotFound
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
from functools import wraps
from sqlalchemy import func
import uuid
#from package.models import User
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


route_code = str(uuid.uuid4())
# print(route_code)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}


posts = []
for i in range(0,10):
    project = {}
    project['title'] = "doggo ipsum"
    #project['img'] = "https://img.buzzfeed.com/buzzfeed-static/static/2017-03/21/7/asset/buzzfeed-prod-fastlane-02/sub-buzz-668-1490096330-22.jpg?downsize=700%3A%2A&output-quality=auto&output-format=auto"
    project['img'] = "https://cdn1.medicalnewstoday.com/content/images/articles/322/322868/golden-retriever-puppy.jpg"
    project['description'] = "Doggo ipsum he made many woofs shoob yapper, you are doing me a frighten. I am bekom fat blep doggo very taste wow boof, I am bekom fat waggy wags clouds ur givin me a spook porgo, heckin angery woofer doing me a frighten you are doin me a concern."
    project['id'] = i
    project['posts'] = {}
    for i in range(0, 5):
        project['posts']['title'] = "Update Number " + str(i)
        project['posts']['body'] = "doggo did a thing"
    posts.append(project)
    # print(posts)


@app.route("/home")
def hello():
    print ("hello there")
    return render_template("home.html", feed = posts)

@app.route("/project", methods = ["GET"])
def project():
    id = request.args["id"]
    proj = {}
    for post in posts:
        if post["id"] == int(id):
            proj = post
    print(proj)
    return render_template("project.html", proj = proj)

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
