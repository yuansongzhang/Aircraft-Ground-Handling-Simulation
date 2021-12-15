#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 20:25:37 2021

@author: duidui
"""

class GatePosition(): #停机位
    def __init__(self,odType,airport,type,id):
        self.odType=odType  #起止类型，即飞机起飞地Origin，飞机目的地Destination
        self.airport=airport    #所属机场
        self.type=type          #远近机位 0近机位，1远机位
        self.id=id              #机位号 012345 0近机位，其它远机位
        
    def getInstance(self):  #按制定重新进行gateposition
        odType="Origin"
        airport="pudong"
        type=1
        id=1
        #print(airport)
        return GatePosition(odType,airport,type,id)
    
    def getAirport(self):
        return self.airport
    
    def getType(self):
        return self.type
    
    def getId(self):
        return self.id
    
    def setAirport(self,airport):
        self.airport=airport
        
    def setType(self,type):
        self.type=type
        
    def setId(self,id):
        self.id=id

        
        