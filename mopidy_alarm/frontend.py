import pykka
from native import time_printer
import time_manager

from mopidy import core

class AlarmFrontend(pykka.ThreadingActor, core.CoreListener):
	def __init__(self, config, core):
		super(AlarmFrontend, self).__init__()
		time_p = time_printer.TimePrinter()
		self.time_manager = time_manager.TimeManager(time_p)
		self.time_manager.update_time()