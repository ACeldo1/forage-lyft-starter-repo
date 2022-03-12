import unittest
from datetime import datetime
from spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def __init__(self):
        self.today = datetime().today().date()
    
    def test_spindler_battery_should_be_serviced(self):
        last_service_date = self.today.replace(year=self.today.year - 3)
        self.assertTrue(SpindlerBattery(self.today, last_service_date).needs_service())
        
    def test_spindler_battery_should_not_be_serviced(self):
        last_service_date = self.today.replace(year=self.today.year - 1)
        self.assertFalse(SpindlerBattery(self.today, last_service_date).needs_service())