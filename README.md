# Team ca-hmoney
It's actually ca$hmoney.

[Watch our video demo here](https://www.youtube.com/watch?v=DXUAyRRkI6k)

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
$ git clone https://github.com/JoshWeiner/ca-hmoney
```
1. Enter the repository
```
$ cd ca-hmoney
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

4. Enter the sub-directory cashmoney
```
$ cd cashmoney
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
 
3. Clone this repository into your root directory

```
$ git clone https://github.com/JoshWeiner/ca-hmoney.git
```

4. Installing pip3 dependencies

```
$ sudo pip3 install -r cashmoney/requirements.txt
```

5. Move the project folder into /var/www

```
$ sudo mv cashmoney /var/www/cashmoney
```

6. Input your droplet IP in the .conf file where it says server adress

7. Put the given .conf file in /etc/apache2/sites-available

8. Enable apache2 and wsgi module

9. Reload and restart apache2
```
$ sudo service apache2 reload
$ sudo service apache2 restart
```
