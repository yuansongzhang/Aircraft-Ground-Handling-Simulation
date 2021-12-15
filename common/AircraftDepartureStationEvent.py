# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 21:30:47 2021

@author: 86191
"""

class AircraftDepartureStationEvent(Event):
    def __init__(self,departureStation,departureTimestamp,nextStationArrivalTimestamp):
        self.departureStation = departureStation
        self.departureTimestamp = departureTimestamp
        self.nextStationArrivalTimestamp = nextStationArrivalTimestamp
        
    def BusDepartureStationEvent(self,bus):
        self.println = println
        if self.println == 1:
            print("--------------------------------------------") 
            print("Generate " + type(self).__name__)
            
    def update(self,**kwargs):    #aircraft
        self.aircraft=aircraft
        self.triggeringTimestamp = aircraft.getScheduledDepartureTime()
        if self.println == 1:
            self.departureStation.info()
            self.aircraft.infoAircraftdepartureStationEvent()
            
        self.updata(self.aircraft)
    
    def execute(self):
#    updates Aircraft.    
        self.Aircraft.AircraftDepartureStationEventUpdate()
        
#    generates next event.
        self.Aircraft.generateAircraftArrivalStationEvent(self.print)