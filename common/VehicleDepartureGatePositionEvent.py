from common import VehicleServiceEvent
from common import Event

class VehicleDepartureArrivalGatePositionEvent(Event):
    "驶离事件"
    def __init__(self,vehicle1,departureTimestamp):
        self.vehicle1=vehicle1
        self.departureTimestamp = departureTimestamp
        
    def update(self):
        self.departureTimestamp = VehicleServiceEvent.serviceFinishTimestamp
        
    def execute(self):
        pass
#    generates next event.     
