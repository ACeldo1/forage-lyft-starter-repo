from battery import Battery

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        # 4 years diff, assuming we are passed in a datetime object for each
        return (self.current_date - self.last_service_date).days >= (365 * 4)