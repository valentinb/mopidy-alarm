import time

class TimeManager():
	'''Manage Time'''

	def __init__(self, time_printer, scheduler):
		self.time_printer = time_printer
		scheduler.add_job(self.update_time, 'interval', minutes=0.01)
		scheduler.start()

	def update_time(self):
		hours   = int(time.strftime("%H", time.localtime()))
		minutes = int(time.strftime("%M", time.localtime()))
		self.time_printer.print_time(hours, minutes)