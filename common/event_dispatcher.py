# -*- coding: utf-8 -*-

class EventDispatcher:
    def __init__(self, aircraft_list):
        self.__aircraft_list = aircraft_list

    def is_finished(self):
        for aircraft in self.__aircraft_list:
            if aircraft.get_current_event() is not None:
                return False
        return True
