from app import db

class User(db.Model):
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
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    userID = db.Column(db.Integer, primary_key=True)
    goal = db.Column(db.Integer, nullable=False)
    current = db.Column(db.Integer, nullable=False)
    projectID = db.Column(db.Integer, nullable = False)
    sID = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Transactions(db.Model):
    dID = db.Column(db.Integer, nullable=False)
    userID = db.Column(db.Integer, nullable = False)
    projectID = db.Column(db.Integer, nullable = False)
    donation = db.Column(db.Integer, nullable=False)
    projects = db.relationship('Projects', backref = 'user', lazy = True)

    def __repr__(self):
        return '<User %r>' % self.username

class Reports(db.Model):
    ##This is the person reporting:
    userID = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String(120), nullable=False)
    projectID = db.Column(db.Integer, nullable = False)
    #This is the person getting reported
    reporteeID = db.Column(db.Integer, nullable = False)
    # Report Number
    reportID = db.Column(db.Integer, primary_key=True)
    reportType = db.Column(db.Integer, nullable = False)


class Messages(db.Model):
    userID = db.Column(db.Integer, nullable = False)
    recieverID = db.Column(db.Integer, nullable = False)
    time = db.Column(db.DateTime, nullable = False)
    body = db.Column(db.String(120), nullable=False)

class Colleges(db.Model):
    sID = db.Column(db.String(120), primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    logo = db.Column(db.String(120), nullable=False)
    color = db.Column(db.String(120), nullable=False)
