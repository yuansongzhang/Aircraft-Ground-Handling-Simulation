# -*- coding: utf-8 -*-
from common import GroundHandlingWaitingEvent
from common import GroundHandlingDispatchEvent
# from .algorithm import random_match
from .algorithm import distance_match


class GroundHandling:
    def __init__(self, aircraft_list, vehicle_list):
        self.__dispatch_interval = 10
        self.__last_dispatch_timestamp = 0
        self.__dispatch_timestamp = None
        self.__aircraft_list = aircraft_list
        self.__vehicle_list = vehicle_list
        self.__event_list = []
        self.__current_event = None
        self.generate_dispatch_event()

    def get_dispatch_timestamp(self):
        return self.__dispatch_timestamp

    def get_current_event(self):
        return self.__current_event

    def set_dispatch_timestamp(self, dispatch_timestamp):
        self.__dispatch_timestamp = dispatch_timestamp

    def set_last_dispatch_time(self, dispatch_timestamp):
        self.__last_dispatch_timestamp = dispatch_timestamp

    def get_last_dispatch_timestamp(self):
        return self.__last_dispatch_timestamp

    def get_dispatch_interval(self):
        return self.__dispatch_interval

    def generate_dispatch_event(self):
        event = GroundHandlingDispatchEvent(self)
        self.__event_list.append(event)
        # update currentEvent.
        self.__current_event = event

    def dispatch_event_update(self):#匹配
        veh_list = []
        for veh in self.__vehicle_list:
            if veh.get_servicestatus() == 0:#空闲
                veh_list.append(veh)
        aircraft_list = []
        for aircraft in self.__aircraft_list:#得到当前调度时间下已知的aircraft
            if aircraft.get_flight().get_category() == 1:#离港
                flight_scheduled_timestamp = aircraft.get_flight().get_scheduled_departure_timestamp()
            else:
                flight_scheduled_timestamp = aircraft.get_flight().get_scheduled_arrival_timestamp()
            if (aircraft.get_status() == 1) & (flight_scheduled_timestamp <= self.__dispatch_timestamp + 4 * 10) == 1:#需要服务且为调度时间戳的后40分钟中
                aircraft_list.append(aircraft)
        # distance_match(self.__dispatch_time, veh_list, aircraft_list)#改
        # random_match(self.__dispatch_timestamp, veh_list, aircraft_list)
        distance_match(self.__dispatch_timestamp, veh_list, aircraft_list)
        
    def generate_waiting_event(self):
        event = GroundHandlingWaitingEvent(self)
        self.__event_list.append(event)
        # update currentEvent.
        self.__current_event = event

    def waiting_event_update(self):
        self.__last_dispatch_timestamp = self.__dispatch_timestamp
