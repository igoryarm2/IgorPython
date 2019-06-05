from datetime import datetime, date, timedelta
tday = datetime.now()
print ("Сегодня: ", datetime.now())
delta_for_day = timedelta(1)
delta_for_month = timedelta(30)
yday = tday - delta_for_day
month_ago = tday - delta_for_month
print("Сейчас: ",tday)
print("Вчера: ",yday)
print("Отмотаем на месяц: ",month_ago)

date_string = '01/01/2017 12:10:03.234567'
date = datetime.strptime(date_string, "%m/%d/%Y %H:%M:%S.%f")
print(date)





# можно ли в timedelta указывать месяца, года? 



#dt_now = datetime.now()
#print(dt_now.strftime('%Y %A %D'))

