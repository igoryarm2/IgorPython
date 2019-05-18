def format_price(price):
    price=int(price)
    price_card = 'Цена: {} руб.'.format(price)
    return price_card
price=float(input("Сколько стоит? ВВОД:"))
print(format_price(price))