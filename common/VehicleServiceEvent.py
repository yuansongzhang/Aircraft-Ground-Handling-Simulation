from vehicle import Vehicle1
from aircraft import Aircraft
from common import Event

class VehicleServiceEvent(Event):
    "服务事件"
    def __init__(self,Vehicle1,Aircraft,servStartTimestamp,servFinishTimestamp):
        self.Vehicle1=Vehicle1;
        self.servStartTimestamp = servStartTimestamp
        self.servFinishTimestamp = servFinishTimestamp
        self.Aircraft = Aircraft
    
    def update(self):
        self.servStartTimestamp = self.Aircraft.getNextStationArrivalTimestamp()
        self.triggeringTimestamp = self.servStartTimestamp
        
    def execute(self):
        self.Vehicle1.finish()
        self.servFinishTimestamp = self.servStartTimestamp+self.Vehicle1.St()
        
        
    
    