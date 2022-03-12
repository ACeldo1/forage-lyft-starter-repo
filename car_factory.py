from abc import ABC
from car import Car
from capulet_engine import CapuletEngine
from willoughby_engine import WilloughbyEngine
from sternman_engine import SternmanEngine
from spindler_battery import SpindlerBattery
from nubbin_battery import NubbinBattery
from carrigan_tires import CarriganTires
from octoprime_tires import OctoprimeTires

class CarFactory(ABC):
    def __init__(self):
        pass
    
    # since a specific type of tire isn't guaranteed with a car model, we need help to determine which tires we are dealing with
    def determine_tires_type(self, name_of_tires, tires_arr):
        if name_of_tires == 'carrigan'.casefold():
            return CarriganTires(tires_arr)
        else: #not sure what te default should be, so I only took into account the 2 mentioned types of tires
            return OctoprimeTires(tires_arr)
    
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, tires_type, tire_conditions):
        tires = self.determine_tires_type(tires_type, tire_conditions)
        calliope = Car(CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(current_date, last_service_date), tires)
        return calliope
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, tires_type, tire_conditions):
        tires = self.determine_tires_type(tires_type, tire_conditions)
        glissade = Car(WilloughbyEngine(current_mileage, last_service_mileage), SpindlerBattery(current_date, last_service_date), tires)
        return glissade

    def create_palindrome(self, current_date, last_service_date, warning_light_on, tires_type, tire_conditions):
        tires = self.determine_tires_type(tires_type, tire_conditions)
        palindrome = Car(SternmanEngine(warning_light_on), SpindlerBattery(current_date, last_service_date), tires)
        return palindrome

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, tires_type, tire_conditions):
        tires = self.determine_tires_type(tires_type, tire_conditions)
        rorschach = Car(WilloughbyEngine(current_date, last_service_date), NubbinBattery(current_date, last_service_date), tires)
        return rorschach

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, tires_type, tire_conditions):
        tires = self.determine_tires_type(tires_type, tire_conditions)
        thovex = Car(CapuletEngine(current_date, last_service_date), NubbinBattery(current_date, last_service_date), tires)
        return thovex