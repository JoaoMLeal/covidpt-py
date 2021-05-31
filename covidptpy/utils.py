from datetime import date, timedelta


def today():
    today_ = date.today()
    return today_.strftime("%d-%m-%Y")


def yesterday():
    yesterday_ = date.today() - timedelta(days=1)
    return yesterday_.strftime("%d-%m-%Y")
