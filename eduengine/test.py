from flask import Flask, render_template, session, request, url_for, redirect, flash

app = Flask(__name__)

projects = []
# print(projects)
for i in range(0, 10):
    # print(i)
    project = {}
    project['title'] = "doggo ipsum"
    #project['img'] = "https://img.buzzfeed.com/buzzfeed-static/static/2017-03/21/7/asset/buzzfeed-prod-fastlane-02/sub-buzz-668-1490096330-22.jpg?downsize=700%3A%2A&output-quality=auto&output-format=auto"
    project['img'] = "https://cdn1.medicalnewstoday.com/content/images/articles/322/322868/golden-retriever-puppy.jpg"
    project['description'] = "Doggo ipsum he made many woofs shoob yapper, you are doing me a frighten. I am bekom fat blep doggo very taste wow boof, I am bekom fat waggy wags clouds ur givin me a spook porgo, heckin angery woofer doing me a frighten you are doin me a concern."
    # print(project)
    projects.append(project)
    # print(projects)


@app.route("/")
def hello():
    print("hello there")
    return render_template("home.html", feed=projects)


@app.route("/s")
def justlook():
    return render_template("base.html")


@app.route("/school")
def pickschool():
    print('find the right school!')
    return render_template("schools.html")


@app.route("/signup")
def poo():
    print('signup')
    return render_template("signup.html")

@app.route('/bigL')
def gotologin():
    return render_template("login.html")

@app.route("/login")
def checkitout(email,pass):
    print('login')
    #check if email is in the database
    #if email in database:
    #   if userId['pass'] == pass:
    #       add in a session
    #       login == true?
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        pass = request.form['pass1']
        fname = request.form['Fname']
        lname = request.form['Lname']
        id = uuid.uuid1()
        user = User(id=id, username=username, email=email, password=pass, firstname=fname, lastname=lname)
        return redirect('/')
    return redirect('/')


@app.route("/sign", methods=["POST", "GET"])
def makenewUser():
    # Sign UP
    print("making user!!")
    if request.method == 'POST':
        # if email in database:
            #flash("you already have an account")
            # redirect('/')
        # elif (pass1 != pass2):
            #flash("Passwords do not match.")
            # redirect('/')
        # else:
            # insert into database
            # email
            # Fname
            # Lname
            # pass1
            # pass2
            # add and commit into db
        print(request.form['email'])
        return redirect('/')
    return redirect('/')
