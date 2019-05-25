def take_figures(one,two):
    if (one != str(one) and two != str(two)):
        print(int(0))
    elif one == two:
        print(int(1))
    elif len(one) > len(two):
        print(int(2))
    elif (one != two and two == 'learn'):
        print(int(3))
One = input("Введите 1-ю строку: ")
Two = input("Введите 2-ю строку: ")
take_figures(One, Two)