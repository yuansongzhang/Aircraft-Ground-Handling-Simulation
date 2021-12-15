#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
import GatePosition  需要吗？？
"""
class Section():
    def __init__(self,type,scheduledDepartureTime,scheduledArrivalTime,
                 origin,destination,realDepartureTime,realArrivalTime):
        self.type=type      #到港离港  0到港 1离港
        self.scheduledDepartureTime=scheduledDepartureTime #预计离开时间
        self.scheduledArrivalTime=scheduledArrivalTime #预计到达时间
        self.origin=origin #出发地
        self.destination=destination, #目的地
        self.realDepartureTime=realDepartureTime #实际离开时间，前期用不到
        self.realArrivalTime=realArrivalTime #实际到达时间，前期用不到
        
    def getInstance(self):
        type=1 #离港
        scheduledDepartureTime="2021-1-1 00:00:00"
        scheduledArrivalTime="2021-1-1 03:00:00"
        origin="pudong"
        destination="hongqiao"
        realDepartureTime="2021-1-1 00:00:00"
        realArrivalTime="2021-1-1 03:00:00"
        return Section(type,scheduledDepartureTime,scheduledArrivalTime,
                       origin,destination,realDepartureTime,realArrivalTime)
    
    def getType(self):
        return self.type
    
    def getScheduledDepartureTime(self):
        return self.scheduledDepartureTime
    
    def getScheduledArrivalTime(self):
        return self.scheduledArrivalTime
    
    def getOrigin(self):
        return self.origin
    
    def getDestination(self):
        return self.destination
    
    def getRealDepartureTime(self):
        return self.realDepartureTime
    
    def getRealArrivalTime(self):
        return self.realArrivalTime
    
    
    
    
    
    
    
    
    
    
    