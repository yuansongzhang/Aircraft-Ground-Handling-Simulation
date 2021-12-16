from common import VehicleServiceEvent
from common import Event

class VehicleDepartureEvent(Event):
    "驶离事件"
    def __init__(self,Vehicle1,leaveTimestamp):
        self.Vehicle1=Vehicle1
        self.leaveTimestamp = leaveTimestamp
        
    def update(self):
        self.leaveTimestamp = VehicleServiceEvent.servFinishTimestamp
        
    def execute(self):
        pass
      
