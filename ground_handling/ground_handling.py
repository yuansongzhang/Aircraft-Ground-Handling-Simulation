# -*- coding: utf-8 -*-
from common import GroundHandlingWaitingEvent
from common import GroundHandlingDispatchEvent
#from .algorithm import distance_match
from .algorithm import random_match


class GroundHandling:
    def __init__(self, aircraft_list, vehicle_list, vehicle_xingli_list, vehicle_jiayou_list, vehicle_baidu_list, vehicle_shipin_list, vehicle_qingshui_list, vehicle_laji_list, vehicle_wushui_list):
        self.__dispatch_interval = 10
        self.__last_dispatch_time = 0
        self.__dispatch_time = None
        self.__aircraft_list = aircraft_list
        self.__vehicle_list = vehicle_list
        self.__vehicle_xingli_list = vehicle_xingli_list
        self.__vehicle_jiayou_list = vehicle_jiayou_list
        self.__vehicle_baidu_list = vehicle_baidu_list
        self.__vehicle_shipin_list = vehicle_shipin_list
        self.__vehicle_qingshui_list = vehicle_qingshui_list
        self.__vehicle_laji_list = vehicle_laji_list
        self.__vehicle_wushui_list = vehicle_wushui_list
        self.__event_list = []
        self.__current_event = None
        self.generate_dispatch_event()

    def get_dispatch_time(self):
        return self.__dispatch_time

    def get_current_event(self):
        return self.__current_event

    def set_dispatch_time(self, dispatch_time):
        self.__dispatch_time = dispatch_time

    def set_last_dispatch_time(self, dispatch_time):
        self.__last_dispatch_time = dispatch_time

    def get_last_dispatch_time(self):
        return self.__last_dispatch_time

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
        veh_xingli_list = []
        for veh in self.__vehicle_xingli_list:
            if veh.get_servicestatus() == 0:#空闲
                veh_xingli_list.append(veh)
        veh_jiayou_list = []
        for veh in self.__vehicle_jiayou_list:
            if veh.get_servicestatus() == 0:#空闲
                veh_jiayou_list.append(veh)
        veh_baidu_list = []
        for veh in self.__vehicle_baidu_list:
            if veh.get_servicestatus() == 0:#空闲
                veh_baidu_list.append(veh)
        veh_shipin_list = []
        for veh in self.__vehicle_shipin_list:
            if veh.get_servicestatus() == 0:#空闲
                veh_shipin_list.append(veh)
        veh_qingshui_list = []
        for veh in self.__vehicle_qingshui_list:
            if veh.get_servicestatus() == 0:#空闲
                veh_qingshui_list.append(veh)
        veh_laji_list = []
        for veh in self.__vehicle_laji_list:
            if veh.get_servicestatus() == 0:#空闲
                veh_laji_list.append(veh)
        veh_wushui_list = []
        for veh in self.__vehicle_wushui_list:
            if veh.get_servicestatus() == 0:#空闲
                veh_wushui_list.append(veh)
        aircraft_list = []
        for aircraft in self.__aircraft_list:#得到当前调度时间下已知的aircraft
            if aircraft.get_flight().get_category() == 1:#离港
                flight_scheduled_time = aircraft.get_flight().get_scheduled_departure_time()
                if (aircraft.get_status() != 0) & (flight_scheduled_time <= self.__dispatch_time + 80) == 1:#需要服务且为调度时间戳的后60分钟中
                #这里的时间需要考虑离港总服务时间+车辆行驶时间等
                    aircraft_list.append(aircraft)
            else:
                flight_scheduled_time = aircraft.get_flight().get_scheduled_arrival_time()
                if (aircraft.get_status() != 0) & (flight_scheduled_time <= self.__dispatch_time + 20) == 1:
                    aircraft_list.append(aircraft)
        random_match(self.__dispatch_time, veh_wushui_list, veh_laji_list, veh_qingshui_list, veh_shipin_list, veh_baidu_list, veh_jiayou_list, veh_xingli_list, veh_list, aircraft_list)
        
    def generate_waiting_event(self):
        event = GroundHandlingWaitingEvent(self)
        self.__event_list.append(event)
        # update currentEvent.
        self.__current_event = event

    def waiting_event_update(self):
        self.__last_dispatch_time = self.__dispatch_time
