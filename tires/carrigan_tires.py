from tires import Tires

class CarriganTires(Tires):
    def __init__(self, tireValues):
        super.__init__()
        self.tireVals = tireValues
        
    def needs_service(self):
        for x in self.tireVals:
            if x >= 0.9: return True
        return False
        # return self.tireVals[0] >= 0.9 or self.tireVals[1] >= 0.9 or self.tireVals[2] >= 0.9 or self.tireVals[3] >= 0.9