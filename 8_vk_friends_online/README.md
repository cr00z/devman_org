# Watcher of Friends Online

It's a simple script to watch of friends "online" in VKontakte social network.

# How to Install

For work you need to register our application in [VK Developers](https://vk.com/dev) and receive APP_ID. After that insert it into script:

```python
APP_ID = 1234567
```

Also you need input authentication data of your personal account in VKontakte (login and password).

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

```bash

$ python vk_friends_online.py
User login: +79777777777
User password: [hidden input]
Александров Александр
Иванов Иван
Сергеев Сергей

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
