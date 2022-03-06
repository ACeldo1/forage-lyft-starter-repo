from abc import ABC, abstractmethod

class Engine(ABC):
    def __init__(self):
        log.debug('Creating an Engine Object...')

    @abstractmethod
    def needs_service(self):
        pass