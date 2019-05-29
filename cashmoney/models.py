from cashmoney import db

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
    ##Lazy loading refers to objects are returned from a
    ##query without the related objects loaded at first.

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
    reports = db.relationship('Report')

    def __repr__(self):
        return '<Project %r>' % self.title


class Transaction(db.Model):
    __tablename__ = "transaction"
    id = db.Column(db.Integer, primary_key=True)
    donor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    donation = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# class Report(db.Model):
#     __tablename__ = "report"
#     ##This is the person reporting:
#     id = db.Column(db.Integer, primary_key=True)
#     reporting_user = db.Column(db.Integer, db.ForeignKey('user.id'))
#     description = db.Column(db.Text(), nullable=False)
#     project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
#     #This is the person getting reported
#     reportee_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     # Report Number
#     report_id = db.Column(db.Integer, primary_key=True)
#     reportType = db.Column(db.Integer, nullable = False)


class Message(db.Model):
    __tablename__ = "message"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    is_sender = db.Column(db.Boolean, nullable=False)
    other_id = db.Column(db.Integer, nullable = False)
    time = db.Column(db.DateTime, nullable = False)
    body = db.Column(db.String(120), nullable=False)

class School(db.Model):
    __tablename__ = "school"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    logo = db.Column(db.String(240), nullable=False)
    color = db.Column(db.String(120), nullable=False)
    members = db.relationship('User')
