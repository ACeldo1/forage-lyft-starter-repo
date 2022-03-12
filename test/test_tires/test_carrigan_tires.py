import unittest
from carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def __init__(self):
        pass
        
    def test_carrigan_tires_should_be_serviced(self):
        tire_conditions = [0, 0, 0, 1]
        carrigan_tires = CarriganTires(tire_conditions)
        self.assertTrue(carrigan_tires.needs_service())

    def test_carrigan_tires_should_not_be_serviced(self):
        tire_conditions = [0, 0, 0, 0]
        carrigan_tires = CarriganTires(tire_conditions)
        self.assertFalse(carrigan_tires.needs_service())