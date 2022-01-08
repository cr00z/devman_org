# Price Formatter

Program presents CLI and functional interface for price formatting.

Inputs string representation of price (such as '12345.678') and outputs user friendly view of it ('12 345.68').

# Quickstart

Example of **format_price.format_price(price)** function usage:

```python

from format_price import format_price
print(format_price('123456.789'))   # out '123 456.79'

```

Example of command line interface on Linux, Python 3.5:

```bash

$ python format_price.py 12345.678
12 345.68

```

Launch of tests:

```bash

$ python tests.py

```

Use in Windows similarly.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
