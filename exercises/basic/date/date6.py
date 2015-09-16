class Date
	__init__(self,day,month,year):
		self.day=day
		self.month=month
		self.year=year
	__add__(days=0, months=0, years=0):
		if type(years)==type(1):
			self.years-=years
		if type(months)==type(1):
			self.months-=months
		if type(days)==type(1):
			self.days-=days
