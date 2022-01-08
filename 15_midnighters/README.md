# Night Owls Detector

Simple Devman API demonstration script.

It determines who sent the tasks to check after midnight.

# How to Install

Python 3 should be already installed. 

Script use [requests](https://pypi.org/project/requests/2.11.1/) and [pytz](https://pypi.org/project/pytz/2019.1/). Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# Quickstart

Example of script launch on Linux, Python 3.5:

```bash

$ python seek_dev_nighters.py
AntonKoltypin
        11.04.2019 00:15:10

constantinovich
        03.04.2019 05:37:06
        02.04.2019 00:43:17
        26.03.2019 00:31:10
        19.03.2019 00:14:57
        13.03.2019 00:03:29

ekluev
        29.03.2019 00:33:43
        29.03.2019 00:21:41
...[skipped]...

```

Use in Windows similarly.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
