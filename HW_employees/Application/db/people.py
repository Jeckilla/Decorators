from Application.db.db import peoples
import os
import datetime
from functools import wraps


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            with open(path, 'a', encoding='utf-8') as f:
                f.write(f'Время начала: {datetime.datetime.now()}\n')
            result = old_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as f:
                f.writelines(f'''Название функции - {old_function.__name__}
Аргументы: {args}, {kwargs}
Функция возвращает: {result}
-----------------------------\n''')
            return result
        return new_function

    return __logger

class Employees():

    def __init__(self):
        print("Класс сотрудников")

    @logger('log_of_get_emp.log')
    def get_employees(self):
        for people in peoples:
            for key, value in people.items():
                print(key, value)
