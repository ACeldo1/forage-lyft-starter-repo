import datetime
from abc import ABC, abstractmethod
from car import Car
from capulet_engine import CapuletEngine
from willoughby_engine import WilloughbyEngine
from sternman_engine import SternmanEngine
from spindler_battery import SpindlerBattery
from nubbin_battery import NubbinBattery

class CarFactory(ABC):
    def __init__(self):

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        calliope = Car(CapuletEngine, Spindler)
        calliope.current_date = current_date
        calliope.last_current_date = last_current_date
        calliope.current_mileage = current_mileage
        calliope.last_service_mileage = last_service_mileage
        return calliope
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        glissade = Car(WilloughbyEngine, SpindlerBattery)
        glissade.current_date = current_date
        glissade.last_current_date = last_current_date
        glissade.current_mileage = current_mileage
        glissade.last_service_mileage = last_service_mileage
        return glissade

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        palindrome = Car(SternmanEngine, SpindlerBattery)
        palindrome.current_date = current_date
        palindrome.last_current_date = last_current_date
        palindrome.warning_light_on = warning_light_on
        return palindrome

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        rorschach = Car(WilloughbyEngine, NubbinBattery)
        rorshcach.current_date = current_date
        rorshcach.last_current_date = last_current_date
        rorshcach.current_mileage = current_mileage
        rorshcach.last_service_mileage = last_service_mileage
        return rorschach

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        thovex = Car(CapuletEngine, NubbinBattery)
        thovex.current_date = current_date
        thovex.last_current_date = last_current_date
        thovex.current_mileage = current_mileage
        thovex.last_service_mileage = last_service_mileage
        return thovex