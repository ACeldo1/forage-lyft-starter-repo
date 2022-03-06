from servicable import Servicable

class Car(Servicable):
    def __init__(self, engine, battery):
        log.debug('Creating a Car Object...')
        self.engine = engine
        self.battery = battery
        super().add_new_car(self)

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()