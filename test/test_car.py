"""
return to this file if there are tests needed that depend specifically on a car model / type, ie: if the Calliope must be changed every 10 years, then we
have to keep track of how old the car is, regardless of the components

while editing this file, I realized that with the initial components provided for each model, this would be valid. However, if a user is allowed
to mix and match, we can have Calliope with a Capulet Engine with a Nubbin battery, and battery tests here will not work
we would need the battery and engine as input here, some notes for myself
"""

import unittest
from datetime import datetime
from car_factory import CarFactory
from serviceable import Serviceable

class TestCalliope(unittest.TestCase):
    def __init__(self):
        self.car_factory = CarFactory()
        self.service = Serviceable()
    
    def test_battery_should_be_serviced(self):
        today = datetime().today().date()
        last_service_date = today.replace(year = today.year - 3)
        car_calliope = self.car_factory.get_calliope(0, 0, today, last_service_date)
        self.assertTrue(self.service(car_calliope).needs_service())
        # self.assertTrue(calliope.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        car_calliope = self.car_factory.get_calliope(0, 0, today, last_service_date)
        self.assertFalse(car_calliope.needs_service())
        # self.assertFalse(self.service(car_calliope).needs_service())
        
    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        car_calliope = self.car_factory.get_calliope(current_mileage, last_service_mileage, last_service_date, last_service_date)
        self.assertTrue(car_calliope.needs_service())
        # self.assertTrue(self.service(car_calliope).needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        car_calliope = self.car_factory.get_calliope(current_mileage, last_service_mileage, last_service_date, last_service_date)
        self.assertFalse(car_calliope.needs_service())
        # self.assertFalse(self.service(car_calliope).needs_service())

class TestGlissade(unittest.TestCase):
    def __init__(self):
        self.car_factory = CarFactory()
        self.service = Serviceable()
    
    def test_battery_should_be_serviced(self):
        today = datetime().today().date()
        last_service_date = today.replace(year = today.year - 3)
        glissade = self.car_factory.get_glissade(0, 0, today, last_service_date)
        self.assertTrue(self.service(glissade).needs_service)
        # self.assertTrue(calliope.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        car_glissade = self.car_factory.get_glissade(0, 0, today, last_service_date)
        self.assertFalse(car_glissade.needs_service())
        self.assertFalse(self.service(car_glissade).needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def __init__(self):
        self.car_factory = CarFactory()
        self.service = Serviceable()
    
    def test_battery_should_be_serviced(self):
        today = datetime().today().date()
        last_service_date = today.replace(year = today.year - 3)
        palindrome = self.car_factory.get_palindrome(today, last_service_date, False)
        self.assertTrue(self.service(palindrome).needs_service)
        # self.assertTrue(calliope.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        car = Palindrome(last_service_date, warning_light_is_on)
        self.assertFalse(car.needs_service())
        self.assertFalse(self.service)

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        car = Palindrome(last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        car = Palindrome(last_service_date, warning_light_is_on)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def __init__(self):
        self.car_factory = CarFactory()
        self.service = Serviceable()
        
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def __init__(self):
        self.car_factory = CarFactory()
        self.service = Serviceable()
    
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
