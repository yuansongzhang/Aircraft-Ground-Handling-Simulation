# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 20:24:47 2021

@author: 86191
"""

class AircraftArrivalStationEvent(Event):
    def __init__(self,arrivalStation,arrivalTimestamp,lastArrivalTimestamp):
        self.=
    
    def BusArrivalStationEvent(self,aircraft,bool print):
        self.print=print
        if self.print:
           print("--------------------------------------------") 
           print("Generate " + type(self).__name__.???)
        self.upate(aircraft)
         
    def update(self,aircraft):
        self.aircraft=aircraft
        self.triggeringTimestamp = aircraft.getNextStationArrivalTimestamp()
        self.arrivalStation = bus.getNextStation();
        self.arrivalTimestamp = self.triggeringTimestamp;
        self.lastArrivalTimestamp = self.arrivalStation.getDepartureTimestamp()
        