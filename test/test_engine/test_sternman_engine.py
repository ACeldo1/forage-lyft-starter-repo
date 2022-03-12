import unittest
from sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def __init__(self):
        self.last_service_mileage = 0
        
    def test_sternman_engine_should_be_serviced(self):
        current_mileage = 30001
        self.assertTrue(SternmanEngine(current_mileage, self.last_service_mileage).needs_service())

    def test_sternman_engine_should_not_be_serviced(self):
        current_mileage = 30000
        self.assertFalse(SternmanEngine(current_mileage, self.last_service_mileage).needs_service())