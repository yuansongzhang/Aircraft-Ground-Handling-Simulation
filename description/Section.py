#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
import GatePosition  需要吗？？
"""
from Line import Line

class Section(): #其中没有type（到港离港  0到港 1离港）
    def __init__(self,scheduledDepartureTime,scheduledArrivalTime,
                 origin,destination,realDepartureTime,realArrivalTime):
        #这里面参数可能有点多
        #self.type=type      #到港离港  0到港 1离港
        self.scheduledDepartureTime=scheduledDepartureTime #预计离开时间
        self.scheduledArrivalTime=scheduledArrivalTime #预计到达时间
        self.origin=origin #出发地
        self.destination=destination, #目的地
        self.realDepartureTime=realDepartureTime #实际离开时间，前期用不到
        self.realArrivalTime=realArrivalTime #实际到达时间，前期用不到
        
    def getInstance(self,line): #参数里需要加line吗？？？？？
        #type=1 #离港
        #line=Line(1)
        scheduledDepartureTime=0
        scheduledArrivalTime=2
        origin=line.getOriginGatePositions()
        destination=line.getDestinationGatePositions()
        realDepartureTime=0
        realArrivalTime=2
        return Section(scheduledDepartureTime,scheduledArrivalTime,
                       origin,destination,realDepartureTime,realArrivalTime)
    
    #def getType(self):
    #    return self.type
    
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
    
    
    
    
    
    
    
    
    
    
    