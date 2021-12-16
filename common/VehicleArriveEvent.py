from common import Event

class VehicleArriveEvent(Event):
    "到达事件"
    def __init__(self,Vehicle1,sessionStartTimestamp,gateArrivalTimestamp):
        self.Vehicle1=Vehicle1
        self.sessionStartTimestamp = sessionStartTimestamp
        self.gateArrivalTimestamp = gateArrivalTimestamp
        
    def update(self):
        self.sessionStartTimestamp=self.Vehicle1.Time
        self.triggeringTimestamp = self.sessionStartTimestamp
        self.Vehicle1.run()
    
    def execute(self):
        self.gateArrivalTimestamp += self.Vehicle1.PreprationTime
           
        
        
