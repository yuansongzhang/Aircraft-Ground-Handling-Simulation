# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 23:51:09 2021

@author: 86191
"""

class Algorithm():
    def __init__(self,aircrafts,vehicles,print):
        self.aircrafts = aircrafts
        self.vehicles = vehicles
    
    def dispatch(self,aircrafts,vehicles):
        for aircraft in self.aircrafts:
            aircraftStatus = (isinstance(aircraft.getCurrentEvent(),aircraftArrivingBlockEvent))
                if aircraftstatus == 1:
                    for vehicle in self.vehicles:
                                vehicleStatus = (isinstance(aircraft.getCurrentEvent(),???))
                                if vehicleStatus == 1:
                                    vehicleMatchAircraft = aircraft.getStationId()
                                    aircraftMatchVehicle = vehicle.getId()

     
#    def isFinished(self):
#        for aircraft in self.aircrafts:
#            status = (isinstance(aircraft.getCurrentEvent(),aircraftFinishingBlockEvent))
#            if status == 0:
#                return False
#        return True
#    
#    def run(self):
#        currentEvent = null
#        finishedAircraftArrayList = list()
#        while self.isFinished() == 0:
#            for aircraft in self.aircrafts:
#                if aircraft in finishedAircraftArrayList:
#                    continue
#            tempEvent = aircraft.getCurrentEvent()    
#        
        
        
        
#        for vehicle in vehicles:
#            if vehicle.getCurrentStatus == free:
#                vehicle.
#                aircraft.
        