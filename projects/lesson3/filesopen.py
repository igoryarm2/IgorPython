with open('Files.txt', 'r', encoding='utf-8') as f:
    context = f.read()
    count_letters = len(context)
    count_words = (len(context.split()))
    changes = context.replace('.', '!')
    print("Количество символов:", count_letters)
    print("Количество слов:", count_words)
with open('File2.txt', 'w', encoding='utf-8') as f:
    print(changes, file=f)