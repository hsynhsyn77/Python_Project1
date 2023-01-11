from datetime import datetime
from datetime import timedelta
# from _datetime import date
# from _datetime import time

# import datetime

simdi = datetime.now()
simdi = datetime.today()

result = datetime.now()
result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = simdi.second

result = datetime.ctime(simdi)
result = datetime.strftime(simdi, "%D")
result = datetime.strftime(simdi, "%X")
result = datetime.strftime(simdi, "%A")
result = datetime.strftime(simdi, "%B")
result = datetime.strftime(simdi, "%d")
result = datetime.strftime(simdi, "%Y,%B,%A")

"""datetime python sitesinden % anlamlarına bakabiliriz """

t = "11 January 2023 hour 12:12:10"
#result = datetime.strptime(t, "%d %B %Y hour %H:%M:%S")
#result = result.year

#birthday = datetime(1978, 12, 7, 12, 30, 00)

#result = datetime.timestamp(birthday)# tarih objesi saniye bilgisi
#result=datetime.fromtimestamp(result)# saniye datetime bilgiisne
#result=datetime.fromtimestamp(0)

#result=simdi - birthday #mtimedelta

#result=result.days
#result=datetime.second
#result=result.microseconds

result=simdi+timedelta(days=10)

result=simdi+timedelta(days=730,seconds=10)

result=simdi-timedelta(days=10)
print(result)
