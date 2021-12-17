#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

main函数需要吗

"""

from GatePosition import GatePosition
import csv


class Line(): #包含单独离开/到达，离开和到达
    def __init__(self,GatePositions):
        self.GatePositions=GatePositions
        self.GatePositionNum=len(self.GatePositions)
        
    def getOriginGatePositions(self):
        return self.GatePositions[0]

    def getDestinationGatePositions(self):
        return self.GatePositions[1]
        #还有一些get没写
    
    def getInstance(self):
        #GatePositionNum=2
        GatePositions=list()
        type=1
        id=1
        GatePositions.append(GatePosition("Origin","pudong",type,id))
        GatePositions.append(GatePosition("Destination","hongqiao",type,id))
        return Line(GatePositions)
    
    def getArriveAndLeaveInstance(self): #还需要再看一看想一想
        lines=list()
        line=Line.getInstance()
        lines.append(line)  #离开浦东机场的线路
        
        GatePositions=list()
        type=1
        id=1
        GatePositions.append(GatePosition("Destination","pudong",type,id))
        GatePositions.append(GatePosition("Origin","hongqiao",type,id))
        lines.append(Line(GatePositions)) #到达浦东机场的线路
        return lines
    
    
    def getFileArriveAndLeaveInstance(self,leave_filename,arrive_filename):
        lines=list() #一个列表，列表中包含2个类，分别是离开路线类，和到达路线类
        
        leaveGatePositionList=list()
        with open (leave_filename,'r') as f:  #在本研究中应该只有2行
            reader = csv.reader(f)
            for row in reader:
                odType=row["odType"]
                airport=row["airport"]
                type=row["type"]
                id=row["id"]
                gatePosition=GatePosition(odType,airport,type,id)
                leaveGatePositionList.append(gatePosition)
        leaveLine=Line(leaveGatePositionList)
        lines.append(leaveLine)

        arriveGatePositionList=list()
        with open (arrive_filename,'r') as f:  #在本研究中应该只有2行
            reader = csv.reader(f)
            for row in reader:
                odType=row["odType"]
                airport=row["airport"]
                type=row["type"]
                id=row["id"]
                gatePosition=GatePosition(odType,airport,type,id)
                arriveGatePositionList.append(gatePosition)
        arriveLine=Line(arriveGatePositionList)
        lines.append(arriveLine)
        
        return lines  #原文件中有set，以及main函数需要吗？
    
    
        
        