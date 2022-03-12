from abc import ABC
from car import Car
from capulet_engine import CapuletEngine
from willoughby_engine import WilloughbyEngine
from sternman_engine import SternmanEngine
from spindler_battery import SpindlerBattery
from nubbin_battery import NubbinBattery

class CarFactory(ABC):
    def __init__(self):
        pass
    
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        calliope = Car(CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(current_date, last_service_date))
        return calliope
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        glissade = Car(WilloughbyEngine(current_mileage, last_service_mileage), SpindlerBattery(current_date, last_service_date))
        return glissade

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        palindrome = Car(SternmanEngine(warning_light_on), SpindlerBattery(current_date, last_service_date))
        return palindrome

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        rorschach = Car(WilloughbyEngine(current_date, last_service_date), NubbinBattery(current_date, last_service_date))
        return rorschach

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        thovex = Car(CapuletEngine(current_date, last_service_date), NubbinBattery(current_date, last_service_date))
        return thovex