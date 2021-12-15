# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 22:06:30 2021

@author: 86191
"""

class Aircraft:
    def __init__(self,aircraftId,lastStation,lastStationArrivalTimestamp,lastStationDepartureTimestamp,
                 nextStation,nextStationArrivalTimestamp,nextStationDepartureTimestamp,eventList,
                 block,println):
        self.aircraftId = aircraftId
        self.lastStation = lastStation  #停机位
        self.lastStationArrivalTimestamp = lastStationArrivalTimestamp
        self.lastStationDepartureTimestamp = lastStationDepartureTimestamp
        self.nextStation = nextStation
        self.nextStationArrivalTimestamp = nextStationArrivalTimestamp
        self.nextStationDepartureTimestamp = nextStationDepartureTimestamp
        self.eventList = eventList
        self.aircraftId = aircraftId
        self.block = block
        #        需要吗？？？
        #        self.tripNum = 0 
        #        self.sectionNum = 0
        self.eventList = list()
        self.lastStation = self.getCurrentSection().getOrigin()
        self.nextStation = self.getCurrentSection().getDestination()
        self.generateAircraftDepartureStationEvent(println)
        

        
    def getInstance(self):      #1个例子
        aircraftId = 0
        return Aircraft(aircraftId)
        
    def getAircraftId(self):
        return aircraftId
#    def getBlock(self):
#        return block
    def getLastStation(self):
        return lastStation
    def getLastStationArrivalTimestamp(self):
        return lastStationArrivalTimestamp
    def getNextStation(self):
        return nextStation
    def getEventList(self):
        return eventList
    def getCurrentEvent(self):
        return self.currentEvent
    def getNextStationArrivalTimestamp(self):
        return self.nextStationArrivalTimestamp
    
    # 生成事件后更新事件
    def generateBusArrivalStationEvent(self,println):
        event = BusArrivalStationEvent(self,println)
        self.eventList.add(event)
        self.currentEvent = event
        
    def aircraftArrivalStationEventUpdate(self):
#        updates section.
        self.getLastSection().setRealArrivalTime(self.getNextStationArrivalTimestamp())
#        updates the aircraft's parameters.
        self.lastStationArrivalTimestamp = self.getNextStationArrivalTimestamp()
        self.lastStation = self.nextStation
        #???如何写
        
    def generateAircraftStoppingStationEvent(self,println):
        event = AircraftStoppingStationEvent(self, println)
        self.eventList.add(event)
        self.currentEvent = event
        
    def aircraftStoppingStationEventUpdate(self):
#        updates the aircraft's parameters.
        #???如何写
        
    def generateAircraftDepartureStationEvent(self,println):
        event = AircraftDepartureStationEvent(self,println)
        self.eventList.add(event)
#        update currentEvent.
        self.currentEvent = event
        
    def aircraftDepartureStationEventUpdate(self):
#        updates the aircraft's parameters.
       #???如何写
       
    def generateAircraftFinishingTripEvent(self,println):
        event = AircraftFinishingTripEvent(self, println)
        self.eventList.add(event)
        self.currentEvent = event
        
    def info(self):
        
    def infoAircraftDepartureStationEvent(self):
    
    def infoAircraftArrivalStationEvent(self):
        


    
    
        