# Anti-Duplicator

Script to find duplicate files (files with the same name and size) on your disk.

# Quickstart

After launch enter the initial path to search.

Important: the search may take some time, do not worry.

The script requires an installed Python interpreter version 3.5, no additional packages required.

Example of script launch on Linux, Python 3.5:

```bash

$ python duplicates.py
Input start path to find duplicates: c:\program files

microba.jar (134366)

c:\program files\JetBrains\IntelliJ IDEA Community Edition 2017.3.5\lib\microba.jar
c:\program files\JetBrains\PyCharm Community Edition 2019.1\lib\microba.jar

rngom-20051226-patched.jar (301200)

c:\program files\JetBrains\IntelliJ IDEA Community Edition 2017.3.5\lib\rngom-20051226-patched.jar
c:\program files\JetBrains\PyCharm Community Edition 2019.1\lib\rngom-20051226-patched.jar

...[output trimmed]...

```

Use in Windows similarly.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
