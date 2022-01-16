# -*- coding: utf-8 -*-

class EventDispatcher:
    def __init__(self, aircraft_list, vehicle_list, ground_handling):
        self.__aircraft_list = aircraft_list
        self.__vehicle_list = vehicle_list
        self.__ground_handling = ground_handling

    def is_finished(self):
        for aircraft in self.__aircraft_list:
            if aircraft.get_current_event() is not None:
                return False
        if self.__vehicle_list is None:
            return True
        else:
            for veh in self.__vehicle_list:
                if veh.get_trip() is not None:
                    return False
        return True
