"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    answer = str(input("Как дела?:\n").capitalize())
    while answer != "Хорошо":
        answer = str(input("Как дела?:\n").capitalize())
    pass

ask_user()
