from mopidy_alarm import time_printer_interface
from i2c_7segments.Adafruit_7Segments import SevenSegments

class TimePrinter(time_printer_interface.TimePrinterInterface):

    def __init__(self):
        self.sevenSegments = SevenSegments()

    def print_time(self, hours, minutes):
        self.sevenSegments.writeDigit(0, int(hours / 10))
        self.sevenSegments.writeDigit(1, hours % 10) 
        self.sevenSegments.writeDigit(3, int(minutes / 10))
        self.sevenSegments.writeDigit(4, minutes % 10)
        self.sevenSegments.setColon(True)

