# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 21:05:37 2021

@author: 86191
"""

class AircraftStoppingStationEvent(Event):
    
    def __init__(self,stoppingStation):
        self.stoppingStation = stoppingStation
        
    def AircraftStoppingStationEvent(self,Aircraft,println):
        self.println = println
        if self.println == 1:
            print("--------------------------------------------") 
            print("Generate " + type(self).__name__)
        
        self.update(aircraft)
        
    def update(self,**kwargs):    #aircraft
        self.aircraft = aircraft
        self.triggeringTimestamp = aircraft.getLastStationArrivalTimestamp()
        self.station = aircraft.getLastStation()
        
        if self.println == 1:
            self.arrivalStation.info()
            self.aircraft.infoAircraftArrivalStationEvent()
       
        self.update(self.aircraft)
        
    def execute(self):
#    updates Aircraft.    
        self.Aircraft.AircraftStoppingStationEventUpdate()
        
#    generates next event.
        self.Aircraft.generateAircraftDepartureStationEvent(self.println)

    