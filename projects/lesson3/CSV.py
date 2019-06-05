import csv
people = [
        {'name': 'Николай', 'age': 34, 'job': 'Доктор'},
        {'name': 'Виктор', 'age': 56, 'job': 'Художник'},
        {'name': 'Анатолий', 'age': 45, 'job': 'Начальник отдела кадров'},
        {'name': 'Елена', 'age':34, 'job': 'Медик'},
        {'name': 'Светлана', 'age': 46, 'job': 'Маркетолог'},
    ]
with open('people.csv', 'w', encoding='utf-8', newline='') as f:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(f, fields, delimiter=':')
    writer.writeheader()
    for employee in people:
        writer.writerow(employee)