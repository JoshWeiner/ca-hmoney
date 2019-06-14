# Team ca-hmoney
It's actually ca$hmoney.

[Watch our video demo here](https://www.youtube.com/watch?v=zxRvoxOktlU)

---

**Project Manager:** Joshua Weiner

**Team Members:** Britni Canale, Max Millar, Kaitlin Wan

---

### Project Description

Our project is meant to be a cross between online networking and crowdfunding site, with a specific focus on colleges. By connecting alumni directly to student clubs, projects, and ventures, we hope to initiate the connection between them to change the way student initiatives are funded. Oftentimes, universities will hand out a limited number of stipends for interested students, but this is in no way a guarantee of funding for anything: from ventures to extra-curricular activities. We believe that instead of donating to some vague, large, endowment, alumni are much more interested in making an impact in similar areas as to what they were interested. The listing on our site hope to connect them to these. Furthermore, for student ventures we hope to partner alumni capital firms with the teams as to generate funding well before any of the traditional structures take place. We hope that the links established via our platform not only help student-ventures circumnavigate the entire mess of startup funding, but also connect interested investors and alumni, as well as help students pursue their interests.

### Features

- Account Creation
- Project Proposal
- Communication
- Chat Functionality

### Necessary packages

Flask-SQLAlchemey, Flask-Migrate

```
pip3 instal sqlalchemy
pip3 instal flask-sqlalchemy
pip3 instal migrate
pip3 instal flask-migrate

```

### Launch Instructions

---

Install and run on localhost

---

0. Clone this repo
```
$ git clone https://github.com/JoshWeiner/ca-hmoney eduengine
```
1. Enter the repository
```
$ cd eduengine
```

2. Create and activate your virtual environment
```
$ python3 -m venv venv
$ . venv/bin/activate
```

3. Install the dependencies
```
$ pip install -r requirements.txt
```

4. Enter the sub-directory eduengine
```
$ cd eduengine
```

5. Initialize the database and migrations folder (where the log of changes to the database is stored)
```
$ flask db init
$ flask db migrate -m "creating database"
$ flasb db upgrade
```

6. Run app
```
$ python __init__.py
```

5. Open your web browser and open `localhost:5000`

7. Use <kbd> CTRL </kbd> + <kbd> C </kbd> to terminate your session in the terminal

8. Type `deactivate` to deactivate your virtual environment

---

Install and run on Apache2

---


0. Ensure you have a working droplet that you have sudo access to.

1. Make sure the droplet is running in ubuntu v18.04 x64

2. Install apache2
```
$ sudo apt install apache2
```
 
3. Navigate to the /var/www directory
```
$ cd /var/www
```

4. Clone this repository into your root directory with the directory name given as "eduengine"
```
$ git clone https://github.com/JoshWeiner/ca-hmoney.git eduengine
```

5. Navigate into the project repository
```
$ cd ./eduengine
```

6. Put .conf file in web serving config folder. Make sure to edit the 'ServerName' within the file to reflect your desired IP address (default is eduengine.stuysu.org)
```
$ sudo cp eduengine.conf /etc/apache2/sites-available
```

7. Navigate into the project subdirectory
```
$ cd ./eduengine
```
*Note: you should now be in /var/www/eduengine/eduengine. PWD to confirm*

8. Create a virtual environment in this folder. This is necessary for the creation and interaction of SQLAlchemy with the database in the project.
```
$ python3 -m venv venv
```

9. Activate the virtual environment
```
$ . venv/bin/activate
```

10. Upgrade pip
```
(venv)$ pip install --upgrade pip
```

11. Install project dependencies. You should currently be within the eduengine directory within the eduengine repository.
```
(venv)$ pip3 install -r ../requirements.txt 
```

12. Initialize the database and migrations folder – to facilitation the insertion or removal of any future database changes
```
(venv)$ flask db init
(venv)$ flask db migrate -m "database creation script"
(venv)$ flask db upgrade
```

13. Deactivate the virtual environment
```
(venv)$ deactivate
```

14. Naviate out of the project to the enclosing folder (var/www) – command should be ```$ cd ../..``` if you have been following deployment instructions exactly.
```
$ cd ../..
```

15. Assign appropriate permissions to the project
```
$ sudo chgrp -R www-data eduengine/
$ sudo chmod -R g+w eduengine/
```

16. Enable Apache2
```
$ sudo a2ensite eduengine
```

17. Enable WSGI
```
$ sudo a2enmod wsgi
```

18. Reload and restart Apache
```
$ systemctl reload apache2
$ sudo service apache2 reload
$ sudo service apache2 restart
```
