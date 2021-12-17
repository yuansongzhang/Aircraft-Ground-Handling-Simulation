from common import Event

class VehicleArrivalGatePositionEvent(Event):
    "到达事件"
    def __init__(self,vehicle1,sessionStartTimestamp,ArrivalGatePositionTimestamp):
        self.vehicle1=vehicle1
        self.sessionStartTimestamp = sessionStartTimestamp
        self.ArrivalGatePositionTimestamp = ArrivalGatePositionTimestamp #到达机位时间戳如何给？
        
    def update(self):
        self.sessionStartTimestamp=self.vehicle1.Time #开始时间
        self.triggeringTimestamp = self.sessionStartTimestamp
        self.vehicle1.run()
    
    def execute(self):
        self.ArrivalGatePositionTimestamp += self.vehicle1.PreprationTime
           
#    generates next event.
        # self.vehicle1.VehicleServiceEvent(self.print)
        
