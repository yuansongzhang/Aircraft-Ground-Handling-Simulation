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
        self.__status = 0#那其实就不用写在前面的括号里了
        if self.__flight.get_category() == 1: #1离港
            self.generate_departure_gate_position_event()
            self.__status = 1
        elif self.__flight.get_category() == 0: #到港
            self.generate_arrival_gate_position_event()
            self.__status = 1

    def get_aircraft_id(self): 
        return self.__aircraft_id

    """
    def get_last_gate_position(self):
        return self.__last_gate_position

    def get_last_gate_position_arrival_timestamp(self):
        return self.__last_gate_position_arrival_timestamp

    def get_next_gate_position(self):
        return self.__next_gate_position
    
    def get_next_gate_position_arrival_timestamp(self):
        return self.__next_gate_position_arrival_timestamp
    """
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
        self.__current_event = None

    def generateAircraftLayoverGatePositionEvent(self):
        pass
        # event = AircraftLayoverGatePositionEvent(self, println)
        # self.__event_list.add(event)
        # self.currentEvent = event

    def aircraftLayoverGatePositionEventUpdate(self):
        pass
