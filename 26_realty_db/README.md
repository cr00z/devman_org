# Real Estate Site

This example work presents:
* simple real estate site
* script to upload advertisement from json fixtures into database

# How to Install

Python 3 should be already installed. 

Script use:
* [Flask](https://pypi.org/project/flask/0.11.1/)
* [Flask-SQLAlchemy](https://pypi.org/project/Flask-SQLAlchemy/2.3.2/)
* [Flask-Migrate](https://pypi.org/project/Flask-Migrate/2.4.0/)

Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Also you need to create sqlite base ...

```bash
$ export FLASK_APP=server.py
$ flask db init
```

... and create and apply migration

```bash
flask db migrate -m "advertisement table"
flask db upgrade
```

# Quickstart

Example of script launch on Linux, Python 3.5:

```bash
$ python load_advert.py ads.json

Advertisements in base (old): 0
Advertisements loaded: 96
Advertisements archived: 0
Advertisements added: 96
```

To run the site application you can use the flask command ...

```bash
$ flask run
```

... and visit http://127.0.0.1:5000/

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
