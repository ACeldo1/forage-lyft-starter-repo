import unittest
from willoughby_engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
    def __init__(self):
        self.last_service_mileage = 0
        
    def test_willoughby_engine_should_be_serviced(self):
        current_mileage = 60001
        self.assertTrue(WilloughbyEngine(current_mileage, self.last_service_mileage).needs_service())

    def test_willoughby_engine_should_not_be_serviced(self):
        current_mileage = 60000
        self.assertFalse(WilloughbyEngine(current_mileage, self.last_service_mileage).needs_service())