# Github Trends

Simple GitHub top repository searcher.

The script finds all repositories created in the last *--days* days (7 by default), selects *--top* of them with the most stars (20 by default) and displays the number of open issues for each.

For unauthenticated requests, the rate limit allows for up to 60 requests per hour. Io increase the rate limit to 6000 per hour, use *--user* parameter and your GitHub credentials. 

# How to Install

Python 3 should be already installed. 

Script use [requests](https://pypi.org/project/requests/2.11.1/). Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# Quickstart

Example of script launch on Linux, Python 3.5:

```bash

$ python github_trending.py --user cr00z --top 5 --days 1
GitHub password:
Please wait
URL                                              STARS ISSUES
https://github.com/tdweiquan/tdw                    37      1
https://github.com/MissFreak/SI-2019-Spring         16      2
https://github.com/shu223/DepthBook                 13      1
https://github.com/kiritoSong/KSSideslipCellDemo    11      0
https://github.com/WittBulter/want                   8      0

```

Use in Windows similarly.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
