# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 08:27:51 2021

@author: 86191
"""
from Event import Event
from Aircraft import Aircraft

class AircraftFinishingTripEvent(Event):
    def __init__(self,aircraft,println):
        self.aircraft = aircraft
        # 还要写什么？？？
        
        if self.println == 1 :
           print("--------------------------------------------") 
           print("Generate " + type(self).__name__)
        self.upate(aircraft)
        
# 更新事件       
    def update(self):    #
        self.triggeringTimestamp = Aircraft.getStoppingStationTimestamp()#+vehicle???
        
# 执行事件   
    def execute(self):
#    updates Aircraft.更新航班执行事件    
        self.Aircraft.AircraftFinishingTripEventUpdate()
        
#    generates next event.生成下一个事件
        self.Aircraft.generateAircraftStoppingStationEvent(self.println)