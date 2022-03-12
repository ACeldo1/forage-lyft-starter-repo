from abc import ABC, abstractmethod
import Logging

class Tires(ABC):
    def __init__(self):
        Logging.debug('Creating a Tires object...')

    @abstractmethod
    def needs_service(self):
        pass