import unittest
from datetime import datetime
from nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def __init__(self):
        self.today = datetime().today().date()
    
    def test_nubbin_battery_should_be_serviced(self):
        last_service_date = self.today.replace(year=self.today.year - 5)
        self.assertTrue(NubbinBattery(self.today, last_service_date).needs_service())
        
    def test_nubbin_battery_should_not_be_serviced(self):
        last_service_date = self.today.replace(year=self.today.year - 3)
        self.assertFalse(NubbinBattery(self.today, last_service_date).needs_service())