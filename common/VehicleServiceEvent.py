from vehicle import vehicle1
from aircraft import aircraft
from common import Event

class VehicleServiceEvent(Event):
    "服务事件"
    def __init__(self,vehicle1,aircraft,serviceStartTimestamp,serviceFinishTimestamp):
        self.vehicle1=vehicle1
        self.aircraft = aircraft
        self.serviceStartTimestamp = serviceStartTimestamp
        self.serviceFinishTimestamp = serviceFinishTimestamp
        
    
    def update(self):
        self.serviceStartTimestamp = self.aircraft.getNextGatePositionArrivalTimestamp()
        self.triggeringTimestamp = self.serviceStartTimestamp
        
    def execute(self):
        self.vehicle1.finish()
        self.serviceFinishTimestamp = self.serviceStartTimestamp+self.vehicle1.ServiceTime()
        
#    generates next event.
        # self.vehicle1.generateVehicleDepartureEvent(self.print)
    
    