"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    Answer = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую"}
    Quest = str(input('Пользователь:').capitalize())
    while Quest != 'Пока':
        try:
            print(Answer.get(Quest,"НЕТ ОТВЕТА. Я тупая машина"))
            Quest = str(input('Пользователь:').capitalize())
        except KeyboardInterrupt: 
            print ('Я не стану это делать')
    pass

ask_user()
