from abc import ABC, abstractmethod
import logging

class Serviceable(ABC):
    exists = False # used if this class is only meant to be called once
    def __init__(self):
        logging.debug('Creating a Servicable Object...')
        self.all_cars = []
        exists = True # same reasoning as above

    def add_new_car(self, new_car):
        self.all_cars.append(new_car)

    @abstractmethod
    def needs_service(self):
        pass