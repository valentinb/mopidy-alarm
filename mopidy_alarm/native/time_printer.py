from mopidy_alarm import time_printer_interface
import os

class TimePrinter(time_printer_interface.TimePrinterInterface):

	def print_time(self, hours, minutes):
		os.system("clear")
		print(str(hours) + ':' + str(minutes))
