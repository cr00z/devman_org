# Решатель квадратных уравнений

Модуль quadratic_equation - универсальный решатель квадратных уравнений

# Как использовать

Функция **get_roots**

Принимает:
* аргументы A, B, C квадратного уравнения.

Возвращает:

* два корня квадратного уравнения.
 
 Для случая двойного корня вместо второго корня возвращает *None*. В случае отрицательного дискриминанта (отсутствия реальных корней) возвращает *(None, None)*. 

Пример использования:

```python
    >>> from quadratic_equation import get_roots
    >>> print(get_roots(1, 2, -3))
    (-3.0, 1.0)
    >>> print(get_roots(1, 2, 1))
    (-1.0, None)
    >>> print(get_roots(1, 2, 3))
    (None, None)
    >>>
```

# Как запустить

Модуль quadratic_equation.py можно запустить с параметрами (coef_A, coef_B, coef_C). Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
quadratic_equation.py 1 2 3 # может понадобиться вызов python3 вместо python, зависит от настроек операционной системы
No real solution
```

Запуск тестов:

```bash
python tests.py
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)