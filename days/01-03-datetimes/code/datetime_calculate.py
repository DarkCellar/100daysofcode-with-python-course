from datetime import date, timedelta, datetime

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""
    result = start_100days + timedelta(days=100)
    return result.strftime("%Y-%m-%d")


def get_days_between_pb_start_first_joint_pycon():
    """Return the int number of days"""
    result = pycon_date - pybites_founded
    return result.days


end_date = get_hundred_days_end_date()
date_difference = get_days_between_pb_start_first_joint_pycon()
print(end_date)
print(date_difference)
