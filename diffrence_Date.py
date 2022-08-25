## Diffrence Between dates in days
import re, datetime
StartDateTime = '2022-08-18T06:54:46.533Z'
d1 = re.split('T', StartDateTime)[0].replace('-', '/')
currentDate = datetime.datetime.now()
d2 = re.split(' ', str(currentDate))[0].replace('-', '/')
d11 = datetime.datetime.strptime(d1, "%Y/%m/%d")
d22 = datetime.datetime.strptime(d2, "%Y/%m/%d")
# difference between dates in timedelta
print(abs(d11-d22).days)
