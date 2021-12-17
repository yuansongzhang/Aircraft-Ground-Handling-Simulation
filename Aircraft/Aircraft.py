# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 22:06:30 2021

@author: 86191
"""

class Aircraft:
    def __init__(self,aircraftId,lastGatePosition,lastGatePositionArrivalTimestamp,lastGatePositionDepartureTimestamp,
                 nextGatePosition,nextGatePositionArrivalTimestamp,nextGatePositionDepartureTimestamp,eventList,
                 block,println):
        self.aircraftId = aircraftId
        self.lastGatePosition = lastGatePosition  #停机位
        self.lastGatePositionArrivalTimestamp = lastGatePositionArrivalTimestamp
        self.lastGatePositionDepartureTimestamp = lastGatePositionDepartureTimestamp
        self.nextGatePosition = nextGatePosition
        self.nextGatePositionArrivalTimestamp = nextGatePositionArrivalTimestamp
        self.nextGatePositionDepartureTimestamp = nextGatePositionDepartureTimestamp
        self.eventList = eventList
        self.aircraftId = aircraftId
        self.block = block
        #        需要吗？？？
        #        self.tripNum = 0 
        #        self.sectionNum = 0
        self.eventList = list()
        self.lastGatePosition = self.getCurrentSection().getOrigin()
        self.nextGatePosition = self.getCurrentSection().getDestination()
        self.generateAircraftDepartureGatePositionEvent(println)
        

        
    def getInstance(self):      #1个例子
        aircraftId = 0
        return Aircraft(aircraftId)
        
    def getAircraftId(self): #可以直接调用参数吗？不定义方法
        return self.aircraftId
#    def getBlock(self):
#        return block
    def getLastGatePosition(self):
        return self.lastGatePosition
    def getLastGatePositionArrivalTimestamp(self):
        return lastGatePositionArrivalTimestamp
    def getNextGatePosition(self):
        return nextGatePosition
    def getEventList(self):
        return eventList
    def getCurrentEvent(self):
        return self.currentEvent
    def getNextGatePositionArrivalTimestamp(self):
        return self.nextGatePositionArrivalTimestamp
    
    # 生成事件后更新事件
    def generateBusArrivalGatePositionEvent(self,println):
        event = BusArrivalGatePositionEvent(self,println)
        self.eventList.add(event)
        self.currentEvent = event
        
    def aircraftArrivalGatePositionEventUpdate(self):
#        updates section.
        self.getLastSection().setRealArrivalTime(self.getNextGatePositionArrivalTimestamp())
#        updates the aircraft's parameters.
        self.lastGatePositionArrivalTimestamp = self.getNextGatePositionArrivalTimestamp()
        self.lastGatePosition = self.nextGatePosition
        #???如何写
        
    def generateAircraftStoppingGatePositionEvent(self,println):
        event = AircraftStoppingGatePositionEvent(self, println)
        self.eventList.add(event)
        self.currentEvent = event
        
    def aircraftStoppingGatePositionEventUpdate(self):
#        updates the aircraft's parameters.
        #???如何写
        
    def generateAircraftDepartureGatePositionEvent(self,println):
        event = AircraftDepartureGatePositionEvent(self,println)
        self.eventList.add(event)
#        update currentEvent.
        self.currentEvent = event
        
    def aircraftDepartureGatePositionEventUpdate(self):
#        updates the aircraft's parameters.
       #???如何写
       
    def generateAircraftFinishingTripEvent(self,println):
        event = AircraftFinishingTripEvent(self, println)
        self.eventList.add(event)
        self.currentEvent = event
        
     def aircraftFinishingTripEventUpdate(self):
 #        updates the aircraft's parameters.
        #???如何写
        
    def info(self):
        
    def infoAircraftDepartureGatePositionEvent(self):
    
    def infoAircraftArrivalGatePositionEvent(self):
        


    
    
        