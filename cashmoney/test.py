from flask import Flask, render_template, session, request, url_for, redirect, flash

app = Flask(__name__)

projects = []
print(projects)
for i in range(0,10):
    print(i)
    project = {}
    project['title'] = "doggo ipsum"
    #project['img'] = "https://img.buzzfeed.com/buzzfeed-static/static/2017-03/21/7/asset/buzzfeed-prod-fastlane-02/sub-buzz-668-1490096330-22.jpg?downsize=700%3A%2A&output-quality=auto&output-format=auto"
    project['img'] = "https://cdn1.medicalnewstoday.com/content/images/articles/322/322868/golden-retriever-puppy.jpg"
    project['description'] = "Doggo ipsum he made many woofs shoob yapper, you are doing me a frighten. I am bekom fat blep doggo very taste wow boof, I am bekom fat waggy wags clouds ur givin me a spook porgo, heckin angery woofer doing me a frighten you are doin me a concern."
    print(project)
    projects.append(project)
    print(projects)

@app.route("/")
def hello():
    print ("hello there")
    return render_template("home.html", feed = projects)

@app.route("/s")
def justlook():
    return render_template("base.html")

@app.route("/school")
def pickschool():
    print('find the right school!')
    return render_template("schools.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
