def Str_compit(one,two):
    if one_str != str(one_str) and two_str != str(two_str):
        print(0)
    elif one_str != two_str and two_str != "learn":
        print(1)
    elif one_str == two_str:
        print(2)
    elif one_str != two_str and two_str == "learn":
        print(3)
one_str = input("Первая строка:")
two_str = input("Вторая строка:")
Str_compit(one_str,two_str)