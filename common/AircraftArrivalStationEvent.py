# -*- coding: utf-8 -*-

from Event import Event
from aircraft import Aircraft

class AircraftArrivalStationEvent(Event):
    def __init__(self,aircraft,arrivalStation,arrivalTimestamp,lastArrivalTimestamp,println):
        self.aircraft = aircraft    #航班
        self.arrivalStation = arrivalStation 
        self.arrivalTimestamp = arrivalTimestamp
        self.lastArrivalTimestamp = lastArrivalTimestamp
        if self.println == 1 :
           print("--------------------------------------------") 
           print("Generate " + type(self).__name__)
        self.upate(aircraft)
 
# 更新事件       
    def update(self):    #
        self.triggeringTimestamp = Aircraft.getNextStationArrivalTimestamp()
        self.arrivalStation = Aircraft.getNextStation();
        self.arrivalTimestamp = self.triggeringTimestamp;
        if self.println == 1:
            self.arrivalStation.info()
            self.aircraft.infoAircraftArrivalStationEvent()
       
# 执行事件   
    def execute(self):
#    updates Aircraft.更新航班执行事件    
        self.Aircraft.AircraftArrivalStationEventUpdate()
        
#    generates next event.生成下一个事件
        self.Aircraft.generateAircraftStoppingStationEvent(self.println)
        