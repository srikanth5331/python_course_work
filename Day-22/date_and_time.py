'''

from datetime import date,time,datetime,time
t = date.today()
print(t)
print("Year:",t.year)
print("Month:",t.month)
print("Day:",t.day)
print("Weekday from 0:",t.weekend())
print("Weekday from 1:",t.isoweekday)

'''
'''
from datetime import date
t = date(2026,12,30)
print(t)
'''

'''
from datetime import time
t = time(23,59,0)
print(t)
'''
'''
from datetime import datetime
t = datetime.now()

print(t)
print("Year:",t.year)
print("Month:",t.month)
print("Day:",t.day)
print("Hour:",t.hour)
print("Minute:",t.minute)
print("Second:",t.second)
'''

'''
from datetime import date,time,datetime,timedelta
n = datetime.now()

print(n.strftime('%d/%m/%y'))
print(n.strftime('%d/%m/%y %H:%M:%S'))
print(n.strftime('%d/%m/%y %I:%M:%S %p'))
print(n.strftime('%d/%b/%y %I:%M:%S %p'))
print(n.strftime('%d/%B/%Y %I:%M:%S %p'))
print(n.strftime('%a, %d/%B/%Y %I:%M:%S %p'))
print(n.strftime('%A, %d/%B/%Y %I:%M:%S %p'))
'''


from datetime import date,time,datetime,timedelta
n = datetime.now()
n15 = n + timedelta(minutes=15)
n2 = n + timedelta(hours=2)
n7 = n+ timedelta(days=60)
print(n15,n2,n7,sep='\n')



































