# Telegram Bot for Pizzeria

This pizza app is designed to accept orders. It consists of:

**Telegram bot** to display the pizzeria menu in the chat.

**Admin interface** for menu modification.

Packages are used:

* Flask
* HTTP Basic Auth (flask_basicauth)
* Database support (flask_sqlalchemy)
* Templates (jinja2)
* Telegram Bot API (pyTelegramBotAPI)
* Migrations (Alembic)

# How to Use

Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Install database tables and initial data:

```bash
$ alembic upgrade head
```

Register new telegram bot for development purposes, get the new token. [@BotFather](https://telegram.me/botfather)

Launch telegram bot:

```bash
$ # the token below is not actual, you need to register a new one
$ export BOT_TOKEN="110831855:AAE_GbIeVAUwk11O12vq4UeMnl20iADUtM"
$ python3 bot.py
```

Run admin interface

```bash
$ export FLASK_APP=server.py
$ flask run
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
