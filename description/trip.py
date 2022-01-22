# -*- coding: utf-8 -*-
from .gate_position import GatePosition


class Trip:
    """The instance of Trip class is produced by GroundHandling class."""

    def __init__(self,
                 task_release_timestamp,
                 #destination: GatePosition,
                 destination_x,
                 destination_y
                 ):
        self.__task_release_timestamp = task_release_timestamp
        self.__destination_x = destination_x
        self.__destination_y = destination_y
        self.__departure_timestamp = None
        self.__arrival_timestamp = None
        self.__service_time = None
        self.__service_finish_timestamp = None
        self.__prepare_time = None
        self.__prepare_finish_timestamp = None
        self.__prepare_start_timestamp = None
        self.__status_turn_to_0_timestamp = None
        
        
    def set_status_turn_to_0_timestamp(self, status_turn_to_0_timestamp):
        self.__status_turn_to_0_timestamp = status_turn_to_0_timestamp
    
    def get_status_turn_to_0_timestamp(self):
        return self.__status_turn_to_0_timestamp
    
    def set_prepare_start_timestamp(self, prepare_start_timestamp):
        self.__prepare_start_timestamp = prepare_start_timestamp
        
    def get_prepare_start_timestamp(self):
        return self.__prepare_start_timestamp

    def set_arrival_timestamp(self, arrival_timestamp):
        self.__arrival_timestamp = arrival_timestamp
        
    def get_arrival_timestamp(self):
        return self.__arrival_timestamp

    def set_departure_timestamp(self, departure_timestamp):
        self.__departure_timestamp = departure_timestamp
    
    def get_depature_timestamp(self):
        return self.__departure_timestamp
    def get_service_time(self):
        return self.__service_time
    def set_service_time(self, service_time):
        self.__service_time = service_time
        
    def set_service_finish_timestamp(self, service_finish_timestamp):
        self.__service_finish_timestamp = service_finish_timestamp
        
    def set_prepare_time(self, prepare_time):
        self.__prepare_time = prepare_time
        
    def set_prepare_finish_timestamp(self, prepare_finish_timestamp):
        self.__prepare_finish_timestamp = prepare_finish_timestamp
        
    def get_service_finish_timestamp(self):
        return self.__service_finish_timestamp
    
    def get_prepare_finish_timestamp(self):
        return self.__prepare_finish_timestamp

    def get_task_release_timestamp(self):
        return self.__task_release_timestamp
    
    def get_destination_x(self):
        return self.__destination_x
    
    def get_destination_y(self):
        return self.__destination_y

    """
    def get_destination(self):
        return self.__destination
    """
    
    def get_departure_timestamp(self):
        return self.__departure_timestamp

    def get_arrival_timestamp(self):
        return self.__arrival_timestamp
