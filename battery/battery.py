from abc import ABC, abstractmethod

class Battery(ABC):
    def __init__(self):
        log.debug('Creating a Battery object...')

    @abstractmethod
    def needs_service(self):
        pass