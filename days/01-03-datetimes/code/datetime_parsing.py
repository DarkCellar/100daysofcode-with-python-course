from datetime import datetime, timedelta
import pytest
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    parsed_line = line.split()
    return datetime.strptime(parsed_line[1], "%Y-%m-%dT%H:%M:%S")


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    sd_initiated_logs = list(filter(lambda x: SHUTDOWN_EVENT in x, loglines))
    first_entry = convert_to_datetime(sd_initiated_logs[0])
    second_entry = convert_to_datetime(sd_initiated_logs[1])
    return second_entry - first_entry
    # shutdown_entries = [line for line in loglines if SHUTDOWN_EVENT in line]
    # shutdown_times = [convert_to_datetime(event) for event in shutdown_entries]
    # return max(shutdown_times) - min(shutdown_times)


def test_convert_to_datetime():
    line1 = 'ERROR 2014-07-03T23:24:31 supybot Invalid user dictionary file'
    line2 = 'INFO 2015-10-03T10:12:51 supybot Shutdown initiated.'
    line3 = 'INFO 2016-09-03T02:11:22 supybot Shutdown complete.'
    assert convert_to_datetime(line1) == datetime(2014, 7, 3, 23, 24, 31)
    assert convert_to_datetime(line2) == datetime(2015, 10, 3, 10, 12, 51)
    assert convert_to_datetime(line3) == datetime(2016, 9, 3, 2, 11, 22)


def test_time_between_events():
    diff = time_between_shutdowns(loglines)
    assert type(diff) == timedelta
    assert str(diff) == '0:03:31'

