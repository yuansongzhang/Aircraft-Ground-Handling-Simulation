# -*- coding: utf-8 -*-
from .gate_position import GatePosition


class Trip:
    """The instance of Trip class is produced by GroundHandling class."""

    def __init__(self,
                 task_release_time,
                 #destination: GatePosition,
                 destination_x,
                 destination_y
                 ):
        self.__task_release_time = task_release_time
        self.__destination_x = destination_x
        self.__destination_y = destination_y
        self.__departure_time = None
        self.__arrival_time = None
        self.__service_time = None
        self.__service_start_time = None
        self.__service_finish_time = None
        self.__prepare_time = None
        self.__prepare_finish_time = None
        self.__prepare_start_time = None
        self.__status_turn_to_0_time = None
    
    def set_service_start_time(self, service_start_time):
        self.__service_start_time = service_start_time
    
    def get_service_start_time(self):
        return self.__service_start_time
        
    def set_status_turn_to_0_time(self, status_turn_to_0_time):
        self.__status_turn_to_0_time = status_turn_to_0_time
    
    def get_status_turn_to_0_time(self):
        return self.__status_turn_to_0_time
    
    def set_prepare_start_time(self, prepare_start_time):
        self.__prepare_start_time = prepare_start_time
        
    def get_prepare_start_time(self):
        return self.__prepare_start_time

    def set_arrival_time(self, arrival_time):
        self.__arrival_time = arrival_time
        
    def get_arrival_time(self):
        return self.__arrival_time

    def set_departure_time(self, departure_time):
        self.__departure_time = departure_time
    
    def get_depature_time(self):
        return self.__departure_time
    def get_service_time(self):
        return self.__service_time
    def set_service_time(self, service_time):
        self.__service_time = service_time
        
    def set_service_finish_time(self, service_finish_time):
        self.__service_finish_time = service_finish_time
        
    def set_prepare_time(self, prepare_time):
        self.__prepare_time = prepare_time
        
    def set_prepare_finish_time(self, prepare_finish_time):
        self.__prepare_finish_time = prepare_finish_time
        
    def get_service_finish_time(self):
        return self.__service_finish_time
    
    def get_prepare_finish_time(self):
        return self.__prepare_finish_time

    def get_task_release_time(self):
        return self.__task_release_time
    
    def get_destination_x(self):
        return self.__destination_x
    
    def get_destination_y(self):
        return self.__destination_y

    """
    def get_destination(self):
        return self.__destination
    """
    
    def get_departure_time(self):
        return self.__departure_time

    def get_arrival_time(self):
        return self.__arrival_time
