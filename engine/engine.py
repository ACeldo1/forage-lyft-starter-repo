from abc import ABC, abstractmethod
import Logging

class Engine(ABC):
    def __init__(self):
        Logging.debug('Creating an Engine Object...')

    @abstractmethod
    def needs_service(self):
        pass