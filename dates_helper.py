import calendar
import time
from datetime import datetime

import pytz
from pandas import datetools as dt


def get_first_day(date_of_interest, d_years=0, d_months=0):
    """
    Get first day of the month for a given date

    :param date_of_interest:
    :param d_years:
    :param d_months:
    :return:
    """
    y, m = date_of_interest.year + d_years, date_of_interest.month + d_months
    a, m = divmod(m - 1, 12)
    result = dt.datetime(y + a, m + 1, 1, 0, 0, 0)
    return result


def get_last_day(date_of_interest):
    """
    Get the last day of the month for a given date

    :param date_of_interest:
    :return:
    """
    result = get_first_day(date_of_interest, 0, 1) - dt.timedelta(days=1)
    return result


def get_tomorrow():
    """
    Get tomorrow's date

    :return:
    """
    time_today = get_today()
    result = time_today + dt.timedelta(days=1)
    return result


def get_yesterday():
    """
    Get yesterday's date

    :return:
    """
    time_today = get_today()
    result = time_today - dt.timedelta(days=1)
    return result


def get_next_by_hour():
    """
    Get the next hour

    :return:
    """
    now = dt.datetime.now()
    result = dt.datetime(now.year, now.month, now.day,
                         now.hour, 0, 0) + dt.timedelta(hours=1)
    return result


def get_today():
    """Get today's midnight

    Returns:
    Date
    """
    now = dt.datetime.today()
    midnight = dt.datetime(now.year, now.month, now.day, 0, 0, 0)

    return midnight


def get_midnight(datetime):
    """
    Get midnight (beginning of day) of a given datetime

    """
    midnight = dt.datetime(datetime.year, datetime.month, datetime.day,
                           0, 0, 0)
    return midnight


def change_timezone_aware(the_date, timezone):
    """
    This takes a date, and ASSUMES its in the timezone passed in and
    make the naive time, timezone aware

    :param the_date:
    :param timezone:
    :return:
    """
    local_tz = pytz.timezone(str(timezone))
    the_date_aware = local_tz.localize(the_date)
    return the_date_aware


def get_now_timestamp_utc():
    """
    Return UTC timestamp

    :return:
    """

    now = calendar.timegm(time.gmtime())

    return now


def convert_ts_iso(t):
    """

    :param t: timestamp
    :return:
    """
    if len(str(t)) == 13:
        t /= 1000

    t = datetime.fromtimestamp(t)
    t = t.strftime('%Y-%m-%d %H:%M:%S%z')
    return t


t = 1478545200000
print("convert_ts_iso: {}".format(convert_ts_iso(t)))
