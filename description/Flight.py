#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 20:46:57 2021

@author: duidui
"""

from Section import Section
from Line import Line

class Flight():     #类似原文件中trip
    def __init__(self,sections,type,leisureTime): #要加ID吗
        #self.id=id #航班号或其它代码
        self.type=type      #到港离港 0到港 1离港
        self.sections=sections
        self.leisureTime=leisureTime #飞机可以停留时间
        
    def getInstance(self,line,startTimeStamp,type,leisureTime): 
        #line=Line(1) #!!
        sections=list()
        scheduledDepartureTime=0+startTimeStamp
        scheduledArrivalTime=2+startTimeStamp #单位h
        origin=line.getOriginGatePositions()
        destination=line.getDestinationGatePositions()
        realDepartureTime=0+startTimeStamp
        realArrivalTime=2+startTimeStamp
        sections.append(Section(scheduledDepartureTime,scheduledArrivalTime,
                                origin,destination,realDepartureTime,realArrivalTime))
        #其实这个sections列表中只有一个Section
        #id="11111"
        #type=1 #离港
        #leisureTime=120 #单位min
        return Flight(sections,type,leisureTime)
    
    def getType(self): #type到港离港
        return self.type
    
    def getLeisureTime(self):
        return self.leisureTime
    
    def getSections(self):
        return self.sections
    
    