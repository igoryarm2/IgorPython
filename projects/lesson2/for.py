"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


students_marks = [
{'school_class': '4a', 'scores': [3,4,4,5,2]},
{'school_class': '4b', 'scores': [5,4,4,2,2]},
{'school_class': '4v', 'scores': [2,3,4,4,3]},
] 
print(type(students_marks))
for school_class in students_marks:
    print(school_class['scores'])
    print(sum(school_class['scores']))
    print(len(school_class['scores']))
    print(sum(school_class['scores'])/len(school_class['scores']))
#Aver = sum(students_marks['scores'])/len(students_marks['scores'])
#pass

