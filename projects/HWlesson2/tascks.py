# Вывести последнюю букву в слове
word = 'Архангельск'
print (word[-1])
print (ord('a')) # Перевод буквы в его код в системы строк

# Вывести количество букв а в слове
word = 'Архангельск'
import pprint
def countLetters(word): 
    y = {} 
    for i in word: 
        if i in y: 
            y[i] += 1
        else: y[i] = 1 
    return y
res1 = countLetters(word)
pprint.pprint(res1)

# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = 0
consonants = 0
for i in word:
    letter = i.lower()
    if letter == "а" or letter == "е" or\
       letter == "и" or letter == "о" or\
       letter == "ё" or letter == "у":
        vowels += 1
    else:
        consonants += 1
print("Vowels %i\nConsonants %i" % (vowels, consonants))



# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
count = 0
flag = 0
for i in range(len(sentence)):
    if sentence[i] != ' ' and flag == 0:
        count += 1
        flag = 1
    else:
        if sentence[i] == ' ':
            flag = 0
print(count)

# 2-й вариант (через преобразование в список):

sentence = sentence.split()
l = len(sentence)
print(l)

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
if sentence[0]!=" ":
    print(sentence[0])
for i in range(len(sentence)):
    if sentence[i]==" ":
        print(sentence[i+1])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
count = 0
flag = 0
aver=0
for i in range(len(sentence)):
    if sentence[i] != ' ':
        count += 1
    else:
        if sentence[i] == ' ' and sentence[i+1] != ' ' :
            aver=aver+count
            count = 0
            flag += 1
print(aver/flag)