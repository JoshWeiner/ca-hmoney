# Team ca-hmoney
It's actually ca$hmoney.

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
-


### Dependencies




### Launch Instructions
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
