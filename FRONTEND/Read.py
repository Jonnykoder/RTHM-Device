

class Read():
    heartRate = 0
    oxySat = 0.0
    bodyTemp = 0.0
    roomTemp = 0.0
    
    def __init__(self, hr  , oxs , bdyTmp , rmpTmp):
        self.heartRate = hr
        self.oxySat = oxs
        self.bodyTemp = bdyTmp
        self.roomTemp =rmpTmp
    def printValues(self):
        print(self.heartRate ,self.oxySat ,self.bodyTemp ,self.roomTemp)

