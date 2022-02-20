# -*- coding: utf-8 -*-
from common import VehicleOtherServiceEvent
from common import VehicleDepartureGatePositionEvent
from common import VehicleArrivalGatePositionEvent
from common import VehicleServiceFinishEvent
from common import VehiclePrepareStartEvent
from common import VehicleStatusTurnTo0Event



class VehicleQingshui:
    def __init__(self,name,v,x,y,aircraft,timestamp,servicestatus):  #x,y,aircraft,timestamp,servicestatus需要变
        self.__name=name;
        self.__v=v;
        self.__x=x;
        self.__y=y;
        self.__servicestatus=servicestatus; #0是空闲 1是在服务
        self.__timestamp=timestamp
        self.__aircraft = None
        self.__trip_list = []
        self.__trip = None
        self.__event_list = list()
        self.__current_event=None
        self.__vehicle_type = 6 #行李车为2，牵引车为1，加油车为3,摆渡车为4，食品车为5，清水车为6
    """  
    def __init__(self, origin):
        self.__origin = origin
        self.__service_time = None
        self.__trip_list = []
        self.__trip = None
        self.__event_list = list()
        self.__current_event = None
    """
    """
    def get_origin(self):   orign统一换成xy
        return self.__origin
    """
    def get_vehicle_type(self):
        return self.__vehicle_type
    
    def get_name(self):
        return self.__name
    
    def set_aircraft(self,aircraft):
        self.__aircraft = aircraft
        
    def get_aircraft(self):
        return self.__aircraft
    
    def get_servicestatus(self):
        return self.__servicestatus
    
    def get_timestamp(self):
        return self.__timestamp
    
    def get_v(self):
        return self.__v
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def set_trip(self, trip):
        self.__trip = trip

    def get_trip(self):
        return self.__trip

    def get_current_event(self):
        return self.__current_event

    def generate_departure_gate_position_event(self):
        event = VehicleDepartureGatePositionEvent(self)
        self.__event_list.append(event)
        # update currentEvent.
        self.__current_event = event
        self.__servicestatus = 1
        
    def departure_gate_position_event_update(self):
        self.__timestamp = self.__trip.get_depature_time()

    def generate_arrival_gate_position_event(self):
        event = VehicleArrivalGatePositionEvent(self)
        self.__event_list.append(event)
        # update currentEvent.
        self.__current_event = event

    def arrival_gate_position_event_update(self):
        self.__x = self.__trip.get_destination_x()
        self.__y = self.__trip.get_destination_y()
        self.__timestamp = self.__trip.get_arrival_time()

    def generate_service_event(self):
        event = VehicleOtherServiceEvent(self)
        self.__event_list.append(event)
        # update currentEvent.
        self.__current_event = event

    def service_event_update(self):
      if self.__trip.get_service_time()==0:
         #self.__aircraft.set_status(1) #????????
         self.__aircraft.set_qingshui_status(1)
         if self.__aircraft.get_flight().get_category()==0:
           self.__aircraft.get_flight().set_scheduled_arrival_time()
         else:
           self.__aircraft.get_flight().set_scheduled_departure_time()
      self.__timestamp = self.__trip.get_service_start_time()

    """    
    def generate_vehicle_return_event(self):
        event = VehicleReturnEvent(self)
        self.__event_list.append(event)
        self.__current_event = event
   """     
    def generate_service_finish_event(self):
        event = VehicleServiceFinishEvent(self)
        self.__event_list.append(event)
        self.__current_event = event
    
    def service_finish_event_update(self):
        self.__timestamp = self.__trip.get_service_finish_time()
        if self.__aircraft.get_flight().get_category()==1: #离港
            self.__aircraft.set_qingshui_status(0) #服务已经完成
            self.__aircraft.set_departure_qingshui_finish_timestamp(self.__timestamp) 
    
    def generate_prepare_start_event(self):
        event = VehiclePrepareStartEvent(self)
        self.__event_list.append(event)
        self.__current_event = event
        
    def prepare_start_event_update(self):
        self.__x = 0 #设车辆统一准备的地点都在0，0
        self.__y = 0
        self.__timestamp = self.__trip.get_prepare_start_time()
        
    def generate_status_turn_to_0_event(self):
        event = VehicleStatusTurnTo0Event(self)
        self.__event_list.append(event)
        self.__current_event = event
    
    def status_turn_to_0_event_update(self):
        self.__timestamp = self.__trip.get_status_turn_to_0_time()
        self.__servicestatus = 0
        self.__trip_list.append(self.__trip)
        self.__trip = None