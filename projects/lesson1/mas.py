dic = {"city": "Москва", "temperature":20}
print(dic["city"])
dic["temperature"]=dic["temperature"]-5
print(dic["temperature"])
print(dic)
print(dic.get("country"))
dic["country"]='Россия'
dic["data"]='27.05.2019'
print(dic)
print(len(dic))