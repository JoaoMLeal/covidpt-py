from datetime import date, timedelta


def today():
    """Returns today's date in the dd-mm-yyyy format"""
    today_ = date.today()
    return today_.strftime("%d-%m-%Y")


def yesterday():
    """Returns yesterday's date in the dd-mm-yyyy format"""
    yesterday_ = date.today() - timedelta(days=1)
    return yesterday_.strftime("%d-%m-%Y")

