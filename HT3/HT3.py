import time
import calendar
a=int(time.time())
sec = 86400
b=int((time.time())/sec)
c=int(b/365)
d=int(c/4)
e=int(((a-((365*40)*sec)-((366*13)*sec))/sec)+1)
print (a, 'current timestamp')
print (b, 'days from Unix start')
print (c, 'years from Unix start')
print (d, 'leap years from Unix start')
print (e, 'th day from the start of this year')

print ('-------------------------------------------------------------------------------------')

from datetime import date
from datetime import datetime

now = datetime.now()
year = now.year
month = now.month
day = now.day

d0 = date(1970, 1, 1)
d1 = date(year, month, day)
delta = d1 - d0
print(delta.days ,'days from Unix start chyotenko edition')

print (int(delta.days/365) ,'years from Unix start chyotenko edition')

d0 = date(2023, 1, 1)
d1 = date(year, month, day)
delta = d1 - d0
print(delta.days +1 ,'days from year start chyotenko edition')

print (calendar.leapdays(y1=1970, y2=2023) ,'leap years from Unix start chyotenko edition')
