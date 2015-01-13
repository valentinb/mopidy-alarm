from __future__ import unicode_literals

import unittest
import mock
from datetime import datetime,date
import time

from mopidy_alarm import time_manager

from testfixtures import Replacer,test_datetime
from testfixtures.tests.sample1 import str_now_1

class TimeTest(unittest.TestCase):

	def test_time_manager_init(self):
		#setup
		time_printer = mock.Mock()
		scheduler = mock.Mock()
		scheduler.add_job = mock.MagicMock()
		#exercize
		sut = time_manager.TimeManager(time_printer, scheduler)
		#check
		scheduler.add_job.assert_called_with(sut.update_time, 'interval', minutes=0.01)

	def test_time_manager_update_time(self):
		#setup
		time_printer = mock.Mock()
		time_printer.print_time = mock.MagicMock()
		scheduler = mock.Mock()
		time.localtime = mock.MagicMock(return_value=time.strptime("10 45", "%H %M"))
		sut = time_manager.TimeManager(time_printer, scheduler)
		#exercize
		sut.update_time()
		#check
		time_printer.print_time.assert_called_with(10, 45)