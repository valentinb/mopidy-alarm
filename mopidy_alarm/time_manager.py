import time

class TimeManager():
	'''Manage Time'''

	def __init__(self, time_printer):
		self.time_printer = time_printer

	def update_time(self):
		hours   = int(time.strftime("%H", time.localtime()))
		minutes = int(time.strftime("%M", time.localtime()))
		self.time_printer.print_time(hours, minutes)