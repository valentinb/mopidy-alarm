import pykka
from apscheduler.schedulers.background import BackgroundScheduler
from native import time_printer
import time_manager
import snooze_manager

from mopidy import core

class AlarmFrontend(pykka.ThreadingActor, core.CoreListener):
	def __init__(self, config, core):
		super(AlarmFrontend, self).__init__()
		printer = time_printer.TimePrinter()
		scheduler = BackgroundScheduler()
		self.time_manager = time_manager.TimeManager(printer, scheduler)
		self.snooze_manager = snooze_manager.SnoozeManager(scheduler)
		scheduler.start()