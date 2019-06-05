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
from flask import render_template, flash, redirect, url_for, request, current_app, abort, jsonify, request, session
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


@app.route('/')
def tohome():
    return redirect('/home')

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

@app.route("/signup")
def poo():
    print('signup')
    #get list of school names
    #get list of school ids
    #jinja render a dropdown for users to select school
    return render_template("signup.html")

@app.route('/bigL')
def gotologin():
    return render_template("login.html")

@app.route("/login")
def checkitout(email,pass):
    print('login')
    email = request.form['email']
    pass1 = request.form['pass1']
    #check if email is in the database
    #if email in database:
    #   if userId['pass'] == pass:
    #       get id from database
    #       add id to session
    #       login == true?
    #    return redirect('/home')
    return redirect('/home')

@app.route("/sign", methods=["POST", "GET"])
def makenewUser():
    # Sign UP
    print("making user!!")
    if request.method == 'POST':
        # if email in database:
            #flash("you already have an account")
            # redirect('/')
        username = request.form['username']
        email = request.form['email']
        pass1 = request.form['pass1']
        pass2 = request.form['pass2']
        fname = request.form['Fname']
        lname = request.form['Lname']
        usert = request.form['usertype']
        # school = request.form['school']
        elif (pass1 != pass2):
            flash("Passwords do not match.")
            redirect('/home')
        id = uuid.uuid1()
        user = User(id=id, username=username, email=email, password=pass1, firstname=fname, lastname=lname, userType=usert, verified=False)
        print(email)
        session.['userid'] = id
        return redirect('/home')
    return redirect('/home')

if __name__ == "__main__":
    app.debug = True
    app.run()
