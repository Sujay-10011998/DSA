from datetime import date

dt = date(1998,1,10)
print("date is: " ,dt)


today = date.today()
print("today's date is: ", today)



from datetime import datetime
DT = datetime.fromtimestamp(123456789)
print("timestamp: ", DT)