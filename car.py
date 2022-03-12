from servicable import Servicable
import Logger

class Car(Servicable):
    def __init__(self, engine, battery, tires):
        Logger.debug('Creating a Car Object...')
        self.engine = engine
        self.battery = battery
        self.tires = tires
        super().add_new_car(self)

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()