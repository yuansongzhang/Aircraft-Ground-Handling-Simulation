# -*- coding: utf-8 -*-
from description import Flight
from common import *


class Aircraft:
    def __init__(self,
                 aircraft_id,
                 flight: Flight,
                 ):
        self.__aircraft_id = aircraft_id
        self.__flight = flight
        self.__event_list = list()
        self.__current_event = None
        if self.__flight.get_category() == 1:
            self.generate_departure_gate_position_event()
        elif self.__flight.get_category() == 0:
            self.generate_arrival_gate_position_event()

    def getAircraftId(self):  # 可以直接调用参数吗？不定义方法
        return self.__aircraft_id

    def getLastGatePosition(self):
        return self.__last_gate_position

    def getLastGatePositionArrivalTimestamp(self):
        return self.__last_gate_position_arrival_timestamp

    def getNextGatePosition(self):
        return self.__next_gate_position

    def getEventList(self):
        return self.__event_list

    def get_current_event(self):
        return self.__current_event

    def getNextGatePositionArrivalTimestamp(self):
        return self.__next_gate_position_arrival_timestamp

    def get_flight(self):
        return self.__flight

    def generate_departure_gate_position_event(self):
        event = AircraftDepartureGatePositionEvent(self)
        self.__event_list.append(event)
        # update currentEvent.
        self.__current_event = event

    def aircraft_departure_gate_position_event_update(self):
        pass

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
