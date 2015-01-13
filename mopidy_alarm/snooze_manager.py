import time
import pygst
import gst

class SnoozeManager():
	'''Manage Snooze'''

	MUSIC_STREAM_URI = 'http://mp3channels.webradio.antenne.de/chillout'
	WAKE_UP_HOUR     = 17
	WAKE_UP_MIN      = 01

	def __init__(self, scheduler):
		self.player = gst.element_factory_make("playbin", "player");
		scheduler.add_job(self.update_snooze, 'interval', minutes=0.01)

	def update_snooze(self):
		hours   = int(time.strftime("%H", time.localtime()))
		minutes = int(time.strftime("%M", time.localtime()))
		if 17 == hours:
			if 02 == minutes:
				self.player.set_property('uri', 'http://mp3channels.webradio.antenne.de/chillout')
				self.player.set_state(gst.STATE_PLAYING)
