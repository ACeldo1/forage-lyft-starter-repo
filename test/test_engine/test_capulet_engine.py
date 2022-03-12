import unittest
from capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def __init__(self):
        self.last_service_mileage = 0
        
    def test_capulet_engine_should_be_serviced(self):
        current_mileage = 30001
        self.assertTrue(CapuletEngine(current_mileage, self.last_service_mileage).needs_service())

    def test_capulet_engine_should_not_be_serviced(self):
        current_mileage = 30000
        self.assertFalse(CapuletEngine(current_mileage, self.last_service_mileage).needs_service())