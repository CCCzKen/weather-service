import time as _t
import datetime


def time():
    return _t.time()


def today():
    return datetime.datetime.today()


def now():
    return datetime.datetime.now()


def format_today(format='%Y%m%d'):
    return datetime.datetime.today().strftime(format)


def strptime(_string, format='%Y-%m-%d %H:%M'):
    return datetime.datetime.strptime(_string, format)


def read_1970_time(str_second, time_format='%Y-%m-%d %H:%M:%S') -> str:
    """
    1970 年至今的秒数转时间
    """
    time_array = _t.localtime(float(str_second))
    return _t.strftime(time_format, time_array)


def is_open_time(_time=None):
    """
    判断是否开市时间
    开市时间: 09:30 - 11:30
             13:00 - 15:00
    """
    if not _time:
        _time = now()

    # 早盘
    if (_time > strptime(str(now().date()) + ' 09:25')) and (_time < strptime(str(now().date()) + ' 11:30')):
        return True

    # 午盘
    if (_time > strptime(str(now().date()) + ' 13:00')) and (_time < strptime(str(now().date()) + ' 15:01')):
        return True

    return False
