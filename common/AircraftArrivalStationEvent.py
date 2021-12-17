# -*- coding: utf-8 -*-

from Event import Event
from aircraft import Aircraft

class AircraftArrivalGatePositionEvent(Event):
    def __init__(self,aircraft,arrivalGatePosition,arrivalTimestamp,lastArrivalTimestamp,println):
        self.aircraft = aircraft    #航班
        self.arrivalGatePosition = arrivalGatePosition 
        self.arrivalTimestamp = arrivalTimestamp
        self.lastArrivalTimestamp = lastArrivalTimestamp
        if self.println == 1 :
           print("--------------------------------------------") 
           print("Generate " + type(self).__name__)
        self.upate(aircraft)
 
# 更新事件       
    def update(self):    #
        self.triggeringTimestamp = Aircraft.getNextGatePositionArrivalTimestamp()
        self.arrivalGatePosition = Aircraft.getNextGatePosition();
        self.arrivalTimestamp = self.triggeringTimestamp;
        if self.println == 1:
            self.arrivalGatePosition.info()
            self.aircraft.infoAircraftArrivalGatePositionEvent()
       
# 执行事件   
    def execute(self):
#    updates Aircraft.更新航班执行事件    
        self.Aircraft.AircraftArrivalGatePositionEventUpdate()
        
#    generates next event.生成下一个事件
        self.Aircraft.generateAircraftStoppingGatePositionEvent(self.println)
        