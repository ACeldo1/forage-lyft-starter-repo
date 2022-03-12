from tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tireValues):
        super.__init__()
        self.tireVals = tireValues
        
    def needs_service(self):
        return sum(self.tireVals) >= 3