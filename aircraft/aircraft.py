# -*- coding: utf-8 -*-
from description import Flight
from common import *


class Aircraft:
    def __init__(self,
                 aircraft_id,
                 flight: Flight,
                 status #1需要服务，0无需服务/服务完成, 2服务正在进行还未完成
                 ):
        self.__aircraft_id = aircraft_id
        self.__flight = flight
        self.__event_list = list()
        self.__current_event = None
        self.__status = 0 #0无需服务/服务完成，1需求服务
        self.__final_departure_timestamp = 1000000000 #初始设置为无穷
        self.__arrive_qianyin_finish_add_timestamp = 10000000000
        self.__arrive_qianyin_start_timestamp = 1000000000
        self.__arrive_baidu_finish_timestamp = 1000000000
        self.__arrive_xingli_finish_timestamp = 1000000000
        self.__arrive_wushui_finish_timestamp = 1000000000
        self.__arrive_laji_finish_timestamp = 1000000000
        self.__departure_xingli_finish_timestamp = 1000000000
        self.__departure_jiayou_finish_timestamp = 1000000000
        self.__departure_baidu_finish_timestamp = 1000000000
        self.__departure_shipin_finish_timestamp = 1000000000
        self.__departure_qingshui_finish_timestamp = 1000000000
        if self.__flight.get_category() == 1: #1离港
            self.generate_departure_gate_position_event()
            self.__status = 1
            self.__xingli_status = 1 #1需要服务，0无需服务/服务完成, 2服务正在进行还未完成
            self.__qianyin_status = 1
            self.__jiayou_status = 1
            self.__baidu_status = 1
            self.__shipin_status = 1
            self.__qingshui_status = 1
            self.__wushui_status = 0
            self.__laji_status = 0
            if self.__flight.get_local_gate_position().get_category()==0:
                self.__baidu_status = 0
                self.set_departure_baidu_finish_timestamp(0)
        elif self.__flight.get_category() == 0: #到港
            self.generate_arrival_gate_position_event()
            self.__status = 1
            self.__xingli_status = 1
            self.__qianyin_status = 1
            self.__jiayou_status = 0
            self.__baidu_status = 1
            self.__shipin_status = 0
            self.__qingshui_status = 0
            self.__wushui_status = 1
            self.__laji_status = 1
            if self.__flight.get_local_gate_position().get_category()==0:
                self.__baidu_status = 0
                self.set_arrive_baidu_finish_timestamp(0)
            
    def set_arrive_wushui_finish_timestamp(self, t):
        self.__arrive_wushui_finish_timestamp = t
        
    def get_arrive_wushui_finish_timestamp(self):
        return self.__arrive_wushui_finish_timestamp
    
    def set_arrive_laji_finish_timestamp(self, t):
        self.__arrive_laji_finish_timestamp = t
        
    def get_arrive_laji_finish_timestamp(self):
        return self.__arrive_laji_finish_timestamp
    
    def set_arrive_xingli_finish_timestamp(self, t):
        self.__arrive_xingli_finish_timestamp = t
        
    def get_arrive_xingli_finish_timestamp(self):
        return self.__arrive_xingli_finish_timestamp
    
    def set_arrive_baidu_finish_timestamp(self, t):
        self.__arrive_baidu_finish_timestamp = t
        
    def get_arrive_baidu_finish_timestamp(self):
        return self.__arrive_baidu_finish_timestamp
    
    def set_arrive_qianyin_finish_add_timestamp(self, t):
        self.__arrive_qianyin_finish_add_timestamp = t
    
    def get_arrive_qianyin_finish_add_timestamp(self):
        return self.__arrive_qianyin_finish_add_timestamp
    
    def set_departure_shipin_finish_timestamp(self, t):
        self.__departure_shipin_finish_timestamp = t
        
    def get_departure_shipin_finish_timestamp(self):
        return self.__departure_shipin_finish_timestamp
    
    def set_departure_qingshui_finish_timestamp(self, t):
        self.__departure_qingshui_finish_timestamp = t
        
    def get_departure_qingshui_finish_timestamp(self):
        return self.__departure_qingshui_finish_timestamp
    
    def set_departure_baidu_finish_timestamp(self, t):
        self.__departure_baidu_finish_timestamp = t
        
    def get_departure_baidu_finish_timestamp(self):
        return self.__departure_baidu_finish_timestamp
    
    def set_departure_xingli_finish_timestamp(self, t):
        self.__departure_xingli_finish_timestamp = t
        
    def get_departure_xingli_finish_timestamp(self):
        return self.__departure_xingli_finish_timestamp
    
    def set_departure_jiayou_finish_timestamp(self, t):
        self.__departure_jiayou_finish_timestamp = t
        
    def get_departure_jiayou_finish_timestamp(self):
        return self.__departure_jiayou_finish_timestamp
    
    def set_qianyin_status(self, status):
        self.__qianyin_status = status
        
    def get_qianyin_status(self):
        return self.__qianyin_status
    
    def set_xingli_status(self, status):
        self.__xingli_status = status
    
    def get_xingli_status(self):
        return self.__xingli_status
    
    def set_jiayou_status(self, status):
        self.__jiayou_status = status
    
    def get_jiayou_status(self):
        return self.__jiayou_status
    
    def set_baidu_status(self, status):
        self.__baidu_status = status
    
    def get_baidu_status(self):
        return self.__baidu_status
    
    def set_shipin_status(self, status):
        self.__shipin_status = status
    
    def get_shipin_status(self):
        return self.__shipin_status
    
    def set_qingshui_status(self, status):
        self.__qingshui_status = status
    
    def get_qingshui_status(self):
        return self.__qingshui_status
    
    def set_wushui_status(self, status):
        self.__wushui_status = status
    
    def get_wushui_status(self):
        return self.__wushui_status
    
    def set_laji_status(self, status):
        self.__laji_status = status
    
    def get_laji_status(self):
        return self.__laji_status
    
    def set_arrive_qianyin_start_timestamp(self, arrive_qianyin_start_timestamp):
        self.__arrive_qianyin_start_timestamp = arrive_qianyin_start_timestamp
    
    def get_arrive_qianyin_start_timestamp(self):
        return self.__arrive_qianyin_start_timestamp
   
    def set_final_departure_timestamp(self, final_departure_timestamp):
        self.__final_departure_timestamp = final_departure_timestamp
        
    def get_final_departure_timestamp(self):
        return self.__final_departure_timestamp
   
    def get_aircraft_id(self): 
        return self.__aircraft_id

    def get_status(self):
        return self.__status
    
    def set_status(self, status):
        self.__status = status

    def get_event_list(self):
        return self.__event_list

    def get_current_event(self):
        return self.__current_event

    def get_flight(self):
        return self.__flight

    def generate_departure_gate_position_event(self):
        event = AircraftDepartureGatePositionEvent(self)
        self.__event_list.append(event)
        # update currentEvent.
        self.__current_event = event

    def aircraft_departure_gate_position_event_update(self):
        self.__current_event = None

    def generate_arrival_gate_position_event(self):
        event = AircraftArrivalGatePositionEvent(self)
        self.__event_list.append(event)
        # update currentEvent.
        self.__current_event = event

    def aircraft_arrival_gate_position_event_update(self):
        pass

    def generate_arrival_service_finish_event(self):
        event = AircraftArrivalServiceFinishEvent(self)
        self.__event_list.append(event)
        self.__current_event = event
        
    def arrival_service_finish_event_update(self):
        self.__current_event = None
