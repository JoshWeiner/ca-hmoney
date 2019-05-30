# -*- coding: utf-8 -*-

from datetime import datetime
import urllib  # for urlopen, urlretrieve
import os      # for chdir, makedirs, path.exists
from flask import render_template, flash, redirect, url_for, request, current_app, abort, jsonify, request
from jinja2 import TemplateNotFound
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
from cashmoney import app, db
from cashmoney.models import User, Project, Transaction, Message, School
from functools import wraps
from sqlalchemy import func
import uuid

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
    posts.append(project)
    print(posts)


@app.route("/home")
def hello():
    print ("hello there")
    return render_template("home.html", feed = posts)

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/students")
def students():
    return render_template("students.html")

@app.route("/schools")
def schols():
    return render_template("schools.html")

from cashmoney import routes, models
