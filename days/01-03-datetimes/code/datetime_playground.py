from datetime import datetime
from datetime import date
from datetime import timedelta


today = datetime.today()
print(str(today))

today_date = today.date()
print(str(today_date))
print(type(today_date))

four_days_later = today.__add__(timedelta(days=4))
print(four_days_later)

print(today_date.__sub__(timedelta(days=4)))



