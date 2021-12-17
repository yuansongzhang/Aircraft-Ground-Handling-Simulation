# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 21:30:47 2021

@author: 86191
"""
from Event import Event
from aircraft import aircraft

class aircraftDepartureStationEvent(Event):
    def __init__(self,aircraft,departureStation,departureTimestamp,nextStationArrivalTimestamp,println):
        self.aircraft = aircraft
        self.departureStation = departureStation
        self.departureTimestamp = departureTimestamp
        self.nextStationArrivalTimestamp = nextStationArrivalTimestamp
        
        self.println = println
        if self.println == 1:
            print("--------------------------------------------") 
            print("Generate " + type(self).__name__)
            
    def update(self,aircraft):    #aircraft
        self.aircraft=aircraft
        self.triggeringTimestamp = aircraft.getScheduledDepartureTime()
        if self.println == 1:
            self.departureStation.info()
            self.aircraft.infoaircraftdepartureStationEvent()
            
        # self.updata(self.aircraft)
    
    def execute(self):
#    updates aircraft.    
        self.aircraft.aircraftDepartureStationEventUpdate()
        
#    generates next event.
        self.aircraft.generateaircraftArrivalStationEvent(self.print)