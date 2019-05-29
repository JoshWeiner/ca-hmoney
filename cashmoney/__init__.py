from flask import Flask, current_app
from threading import Thread
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import current_app
#from wtf_tinymce import wtf_tinymce
from config import Config
from time import sleep
import datetime
import os

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from cashmoney import routes, models
