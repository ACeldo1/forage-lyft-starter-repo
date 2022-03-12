import unittest
from octoprime_tires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):
    def __init__(self):
        pass
        
    def test_octoprime_tires_should_be_serviced(self):
        tire_conditions = [1, 1, 1, 0]
        octoprime_tires = OctoprimeTires(tire_conditions)
        self.assertTrue(octoprime_tires.needs_service())

    def test_octoprime_tires_should_not_be_serviced(self):
        tire_conditions = [0, 1, 0, 1]
        octoprime_tires = OctoprimeTires(tire_conditions)
        self.assertFalse(octoprime_tires.needs_service())