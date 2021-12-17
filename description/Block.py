#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 21:42:54 2021

@author: duidui
"""

from Flight import Flight

class Block():
    def __init__(self,flights):
        self.flights=flights
        
    def getInstance(self,arriveLine,leaveLine,startTimestamp,leisureTime):
        flights=list()
        flights.append(Flight.getInstance(arriveLine,startTimestamp,0,leisureTime))
        flights.append(Flight.getInstance(leaveLine,startTimestamp,1,leisureTime))
