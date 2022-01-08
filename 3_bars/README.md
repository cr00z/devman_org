# Ближайшие бары

Скрипт обрабатывает список московских баров с сайта [data.mos.ru](https://data.mos.ru/) и возвращает:

* самый большой бар;
* самый маленький бар;
* самый близкий бар (текущие gps-координаты пользователь вводит с клавиатуры).

Уже скачанный список можно взять на [devman.org](https://devman.org/fshare/1503831681/4/).

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py # possibly requires call of python3 executive instead of just python
Biggest bar: Спорт бар «Красная машина»
Smallest bar: БАР. СОКИ
Input your latitude: 55.68
Input your longitude: 37.63
Closest bar: Магазин-Бар «Бирстон»

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
