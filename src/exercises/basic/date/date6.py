# CHECK_WITH python2


class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __add__(days=0, months=0, years=0):
        if isinstance(years, int):
            self.years -= years
        if isinstance(months, int):
            self.months -= months
        if isinstance(days, int):
            self.days -= days
