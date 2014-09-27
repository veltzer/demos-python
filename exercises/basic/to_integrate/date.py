class Date:
	days_in_months=[31,29,31,30,31,30,31,31,30,31,30,31]
	def __init__(self, day, month, year):
		if ( (type(day)!=type(1)) or (type(month)!=type(1)) or (type(year)!=type(1))):
			print('Date must be initialized with numbers')
			return
		if ((month<1) or (month>12)):
			print('Month must be between 1 and 12')
			return
		if ( (day<0) or (day>self.days_in_months[month-1])):
			print('Day must be between 1 and ', self.days_in_months[month-1])
			return
		self.day=day
		self.month=month
		self.year=year
	def __gt__(self,other):
		''' Overloading operator>for dates '''
		if (self.year>other.year):
			return True
		elif (self.year==other.year):
			if (self.month>other.month):
				return True
			elif (self.month==other.month):
				if(self.day>other.day):
					return True
		return False
	def __lt__(self,other):
		''' Overloading operator<for dates '''
		return other>self
	def __eq__(self,other):
		''' Overloading operator==for dates '''
		return ((self.year==other.year) and (self.month==other.month) and (self.day==other.day))
	def __ne__(self,other):
		''' Overloading operator!=for dates '''
		return not (self==other)
	def __le__(self,other):
		''' Overloading operator<=for dates '''
		return (self<other) or (self==other)
	def __ge__(self,other):
		''' Overloading operator>=for dates '''
		return (self>other) or (self==other)
	def __str__(self):
		return str(self.day)+'.'+str(self.month)+'.'+str(self.year)
