import pytest
from datetime import datetime

THIS_YEAR = 2018


def years_ago(date):
    """Receives a date string of 'DD MMM, YYYY', for example: 8 Aug, 2015
       Convert this date str to a datetime object (use strptime).
       Then extract the year from the obtained datetime object and subtract
       it from the THIS_YEAR constant above, returning the int difference.
       So in this example you would get: 2018 - 2015 = 3"""
    converted_date = datetime.strptime(date, "%d %b, %Y")
    return THIS_YEAR - converted_date.year


def convert_eu_to_us_date(date):
    """Receives a date string in European format of dd/mm/yyyy, e.g. 11/03/2002
       Convert it to an American date: mm/dd/yyyy (in this case 03/11/2002).
       To enforce the use of datetime's strptime / strftime (over slicing)
       the tests check if a ValueError is raised for invalid day/month/year
       ranges (no need to code this, datetime does this out of the box)"""
    converted_date = datetime.strptime(date, "%d/%m/%Y")
    return converted_date.strftime("%m/%d/%Y")


def test_years_ago():
    assert years_ago('8 Aug, 2015') == 3
    assert years_ago('6 Sep, 2014') == 4
    assert years_ago('1 Oct, 2010') == 8
    assert years_ago('31 Dec, 1958') == 60


def test_convert_eu_to_us_date():
    assert convert_eu_to_us_date('11/03/2002') == '03/11/2002'
    assert convert_eu_to_us_date('18/04/2008') == '04/18/2008'
    assert convert_eu_to_us_date('12/12/2014') == '12/12/2014'
    assert convert_eu_to_us_date('1/3/2004') == '03/01/2004'
