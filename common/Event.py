# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 20:36:42 2021

@author: 86191
"""

from abc import ABCMeta, abstractmethod

class Event():
    __meta_class__ = ABCMeta
    
    def __init__(self,triggeringTimestamp,aircraft,vehicle,algorithm,print):
        self.triggeringTimestamp = triggeringTimestamp
        self.aircraft = aircraft
        self.vehicle = vehicle
        self.algorithm = algorithm
    
    @abstractmethod    
    def update(self,aircraft,vehicle,algorithm):
        pass
    
    @abstractmethod
    def update(self):   
        pass
    
    @abstractmethod   
    def execute(self): 
        pass
        
    @abstractmethod    
    def info(self):
        pass