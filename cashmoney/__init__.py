import sys
from flask import Flask, current_app
from threading import Thread
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import current_app
#from wtf_tinymce import wtf_tinymce
#import setup
# print(package.config)
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
from threading import Thread
#from package.models import User
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.urandom(32)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


route_code = str(uuid.uuid4())
# print(route_code)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120))
    userType = db.Column(db.Integer, nullable=False)
    paypal = db.Column(db.String(250))
    verified = db.Column(db.Boolean, nullable=False)
    school = db.Column(db.Integer, db.ForeignKey('school.id'))
    pic = db.Column(db.Text())
    projects = db.relationship('Project')
    # reports_made = db.relationship('Report', foreign_keys=['reports.reporting_user'])
    # reports_against = db.relationship('Report', foreign_keys=['reports.reportee_id'])
    messages = db.relationship('Message')
    # Lazy loading refers to objects are returned from a
    # query without the related objects loaded at first.

    def __repr__(self):
        return '<User %r>' % self.username


class Project(db.Model):
    __tablename__ = "project"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text())
    goal = db.Column(db.Float)
    current_amount = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    school_id = db.Column(db.String(120), db.ForeignKey('school.id'))
    transactions = db.relationship('Transaction')
    # reports = db.relationship('Report')
    def __repr__(self):
        return '<Project %r>' % self.title


class Transaction(db.Model):
    __tablename__ = "transaction"
    id = db.Column(db.Integer, primary_key=True)
    donor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    donation = db.Column(db.Float, nullable=False)
    confirmed = db.Column(db.Boolean)
    def __repr__(self):
        return '<User %r>' % self.username


class Message(db.Model):
    __tablename__ = "message"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    is_sender = db.Column(db.Boolean, nullable=False)
    other_id = db.Column(db.Integer, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    body = db.Column(db.String(120), nullable=False)


class School(db.Model):
    __tablename__ = "school"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    logo = db.Column(db.String(240), nullable=False)
    color = db.Column(db.String(120), nullable=False)
    members = db.relationship('User')


'''
posts = []
for i in range(0,10):
    project = {}
    project['title'] = "doggo ipsum"
    #project['img'] = "https://img.buzzfeed.com/buzzfeed-static/static/2017-03/21/7/asset/buzzfeed-prod-fastlane-02/sub-buzz-668-1490096330-22.jpg?downsize=700%3A%2A&output-quality=auto&output-format=auto"
    project['img'] = "https://cdn1.medicalnewstoday.com/content/images/articles/322/322868/golden-retriever-puppy.jpg"
    project['description'] = "Doggo ipsum he made many woofs shoob yapper, you are doing me a frighten. I am bekom fat blep doggo very taste wow boof, I am bekom fat waggy wags clouds ur givin me a spook porgo, heckin angery woofer doing me a frighten you are doin me a concern."
    project['id'] = i
    posts.append(project)
    # print(posts)
'''

users = []
for i in range(0, 5):
    user = {}
    user['id'] = i
    user['name'] = "Doge Numero " + str(i)
    user['school'] = "Doggo University School of Boops"
    users.append(user)


@app.route('/')
def tohome():
    return redirect('/home')


@app.route("/home")
def hello():
    try:
        print("hello there, user number " + session['user_id'])
    except:
        print('hello there, user without identification')
    i = 0
    posts = []
    for u in Project.query.all():
        if i > 10:
            break
        posts.append(u.__dict__)
        posts[i]['img'] = "https://cdn1.medicalnewstoday.com/content/images/articles/322/322868/golden-retriever-puppy.jpg"
        i += 1
    print(session)
    loggedin = False
    try:
        if session['user_id'] is None:
            loggedin = False
        elif (session['user_id'] is not None and session['user_id'] is not 0):
            loggedin = True
    except:
        loggedin =False
    return render_template("home.html", feed=posts, users=users, loggedin=loggedin)


@app.route("/project", methods=["GET"])
def project():
    id = request.args["id"]
    proj = Project.query.filter_by(id=id).first()
    proj['img'] = "https://cdn1.medicalnewstoday.com/content/images/articles/322/322868/golden-retriever-puppy.jpg"
    #user = db.session.query(User).filter_by(id=proj['user_id']).first().__dict__
    user = proj['user_id']
    loggedin = False
    try:
        if session['user_id'] is None:
            loggedin = False
        elif (session['user_id'] is not None and session['user_id'] is not 0):
            loggedin = True
    except:
        loggedin =False
    return render_template("project.html", proj=proj, user=user, loggedin=loggedin)

@app.route("/logout")
def logout():
    session['user_id'] = 0
    # session['user_id'] = 0
    flash("Successfully logged out!")
    return redirect("/home")

@app.route("/projects")
def projects():
    loggedin = False
    try:
        if session['user_id'] is None:
            loggedin = False
        elif (session['user_id'] is not None and session['user_id'] is not 0):
            loggedin = True
    except:
        loggedin =False
    return render_template("projects.html", loggedin = loggedin)


@app.route("/students")
def students():
    loggedin = False
    try:
        if session['user_id'] is None:
            loggedin = False
        elif (session['user_id'] is not None and session['user_id'] is not 0):
            loggedin = True
    except:
        loggedin =False
    return render_template("students.html", loggedin=loggedin)


@app.route("/schools")
def schols():
    loggedin = False
    try:
        if session['user_id'] is None:
            loggedin = False
        elif (session['user_id'] is not None and session['user_id'] is not 0):
            loggedin = True
    except:
        loggedin =False
    return render_template("schools.html", loggedin=loggedin)


@app.route("/signup")
def poo():
    print('signup')
    # get list of school names
    # get list of school ids
    # jinja render a dropdown for users to select school
    loggedin = False
    try:
        if session['user_id'] is None:
            loggedin = False
        elif (session['user_id'] is not None and session['user_id'] is not 0):
            loggedin = True
    except:
        loggedin =False
    if loggedin:
        flash("You must be logged out to access this page!")
        return redirect("/home")
    else:
        return render_template("signup.html", loggedin=loggedin)

@app.route('/login', methods=["GET", "POST"])
def login():
    loggedin = False
    try:
        if session['user_id'] is None:
            loggedin = False
        elif (session['user_id'] is not None and session['user_id'] is not 0):
            loggedin = True
    except:
        loggedin =False
    if not loggedin:
        if request.method == "POST":
            givenemail = request.form.get('email')
            username = request.form.get('email')
            pass1 = request.form.get('pass')
            exists = User.query.filter_by(email=givenemail).first()
            # print(User.query.all())
            if exists is not None:
                if pass1 == exists.password:
                    session["user_id"] = exists.id
                    return redirect("/home")
                else:
                    flash("Username or password is incorrect.")
                    return redirect("/login")
            else:
                exists = User.query.filter_by(username=username).first()
                # print(exists)
                if exists is not None:
                    if pass1 == exists.password:
                        session["user_id"] = exists.id
                        return redirect("/home")
                    else:
                        flash("Username or password is incorrect.")
                        return redirect("/login")
                else:
                    flash("Username or password is incorrect.")
                    return redirect("/login")
        return render_template("login.html", loggedin = loggedin)
    else:
        flash("You must be logged out to access this page!")
        return redirect("/home")

@app.route("/sign", methods=["GET", "POST"])
def makenewUser():
    loggedin = False
    try:
        if session['user_id'] is None:
            loggedin = False
        elif (session['user_id'] is not None and session['user_id'] is not 0):
            loggedin = True
    except:
        loggedin =False
    # Sign UP
    # print("making user!!")
    if not loggedin:
        if request.method == 'POST':
            # if email in database:
                #flash("you already have an account")
                # redirect('/')
            username = str(request.form.get('username'))
            email = str(request.form.get('email'))
            pass1 = str(request.form.get('pass1'))
            pass2 = str(request.form.get('pass2'))
            fname = str(request.form.get('Fname'))
            lname = str(request.form.get('Lname'))
            usert = int(request.form.get('usertype'))
            register_failed = False
            # school = request.form['school']
            # print(User.query.filter_by(email=email).first())
            if (pass1 != pass2):
                flash("Passwords do not match.")
                register_failed = True
            if (User.query.filter_by(email=email).first() is not None):
                flash("This email was already registered with another user.")
                register_failed = True
            if (User.query.filter_by(username=username).first() is not None):
                flash("Username already taken")
                register_failed = True
            if (register_failed):
                return redirect("/sign")
            else:
                user = User(username=username, email=email, password=pass1, firstname=fname, lastname=lname, userType=usert, verified=False)
                # pprint(user)
                db.session.add(user)
                db.session.commit()
                return redirect("/login")
            #You do not need to specfy ID, SQL automatically generates one
            #user = User(username=username, email=email, password=pass1, firstname=fname, lastname=lname, userType=usert, verified=False)
            #session['userid'] = id
        return render_template("signup.html", loggedin=loggedin)
    else:
        flash("You must be logged out to access this page!")
        return redirect("/home")


@app.route('/makeproject')
def makeprojectpage():
    loggedin = False
    try:
        if session['user_id'] is None:
            loggedin = False
        elif (session['user_id'] is not None and session['user_id'] is not 0):
            loggedin = True
    except:
        loggedin =False
    if not loggedin:
        flash("You must be logged in to access this page!")
        return redirect("/login")
    else:
        return render_template('makeproject.html', loggedin=loggedin)


@app.route('/processproject', methods=['POST', 'GET'])
def processproject():
    title = request.form.get('title')
    description = request.form.get('description')
    goal = request.form.get('goal')
    # add userid and schoolid once sessions get back
    project = Project(title=title, description=description,
                      goal=goal, current_amount=0.0)
    db.session.add(project)
    db.session.commit()
    return redirect('/')


@app.route('/user/<id>')
def userpage(id):
    user = User.query.filter_by(id=id).first()
    i = 0
    posts = []
    for u in Project.query.all():
        if i > 10:
            break
        posts.append(u.__dict__)
        posts[i]['img'] = "https://cdn1.medicalnewstoday.com/content/images/articles/322/322868/golden-retriever-puppy.jpg"
        i += 1
    print(posts)
    return render_template('user.html', user=user, posts=posts)

@app.route('/chat', methods=['POST', 'GET'])
def chat():
    loggedin = False
    try:
        if session['user_id'] is None:
            loggedin = False
        elif (session['user_id'] is not None and session['user_id'] is not 0):
            loggedin = True
    except:
        loggedin =False
    if not loggedin:
        flash("You must be logged in to access this page!")
        return redirect("/login")
    else:
        messages = Message.query.all()
        users_with_chat = []
        all_users = User.query.all()
        for message in messages:
            if message.user_id == session['user_id']:
                u = User.query.filter_by(id=message.other_id).first()
                if u not in users_with_chat:
                    users_with_chat.append(u)
            if message.other_id == session['user_id']:
                u = User.query.filter_by(id=message.user_id).first()
                if u not in users_with_chat:
                    users_with_chat.append(u)
        # print(session)
        u = User.query.filter_by(id=session['user_id']).first()
        return render_template('chat_users.html', u=u, users=users_with_chat, all_users=all_users, loggedin=loggedin)

@app.route("/get_user_by_id", methods = ["POST"])
def get_user_by_id():
    this = request.form['query_id']
    # print(this)
    user = User.query.filter_by(id=this).first()
    # print(user)
    return jsonify({
        "id": user.id,
        "username" : user.username,
        "firstname": user.firstname,
        "lastname": user.lastname
    })

def add_async_message(app, msg):
    with app.app_context():
        db.session.add(msg)
        db.session.commit()

@app.route("/send_message", methods=["POST"])
def send_message():
    to_id = request.form['to_id']
    from_id = request.form['from_id']
    msg = request.form['rawText']
    is_sender = True
    if to_id != session["user_id"]:
        is_sender = False
    Thread(target=add_async_message, args=(app, Message(user_id=from_id, is_sender=is_sender, other_id=to_id, time=datetime.now(), body=msg))).start()
    db.session.add(m)
    db.session.commit()
    return "True"

@app.route("/retrieve_messages", methods=["POST"])
def retrieve_messages():
    to_id = request.form.get('to_id')
    from_id = request.form.get('from_id')
    msgs = Message.query.filter_by(user_id = from_id, other_id=to_id).all()
    newmsgs = Message.query.filter_by(user_id = to_id, other_id=from_id).all();
    for m in newmsgs:
        if m not in msgs:
            msgs.append(m)
    # msgs.sort(key lambda x: x.id)
    msgs = sorted(msgs, key=lambda x:x.id)
    # print(msgs)
    b = []
    for m in msgs:
        # print(m, m.id)
        if m is not None:
            a = {
                "from_id" : m.user_id,
                "to_id" : m.other_id,
                "body" : m.body
            }
            b.append(a)
    return jsonify({
        'messages' : b})

if __name__ == "__main__":
    app.debug = True
    app.run()
