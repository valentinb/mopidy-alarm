from __future__ import unicode_literals

import unittest
import mock
from datetime import datetime,date
import time

from mopidy_alarm import snooze_manager

from testfixtures import Replacer,test_datetime
from testfixtures.tests.sample1 import str_now_1

class SnoozeTest(unittest.TestCase):

	def test_snoozee_manager_init(self):
		#setup
		scheduler = mock.Mock()
		scheduler.add_job = mock.MagicMock()
		#exercize
		sut = snooze_manager.SnoozeManager(scheduler)
		#check
		scheduler.add_job.assert_called_with(sut.update_snooze, 'interval', minutes=0.5)