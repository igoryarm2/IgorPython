def Str_compit(one,two):
    if one != str(one) and two != str(two):
        print(0)
    elif one != two and len(two) <= len(one):
        print(1)
    elif one == two:
        print(2)
    elif one != two and two == "learn":
        print(3)
one_str = input("Первая строка:")
two_str = input("Вторая строка:")
Str_compit(one_str,two_str)