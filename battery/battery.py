from abc import ABC, abstractmethod
import Logging

class Battery(ABC):
    def __init__(self):
        Logging.debug('Creating a Battery object...')

    @abstractmethod
    def needs_service(self):
        pass