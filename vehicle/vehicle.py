# -*- coding: utf-8 -*-
from common import VehicleServiceEvent
from common import VehicleDepartureGatePositionEvent
from common import VehicleArrivalGatePositionEvent


class Vehicle:
    def __init__(self, origin):
        self.__origin = origin
        self.__service_time = None
        self.__trip_list = []
        self.__trip = None
        self.__event_list = list()
        self.__current_event = None

    def get_origin(self):
        return self.__origin

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

    def departure_gate_position_event_update(self):
        pass

    def generate_arrival_gate_position_event(self):
        event = VehicleArrivalGatePositionEvent(self)
        self.__event_list.append(event)
        # update currentEvent.
        self.__current_event = event

    def arrival_gate_position_event_update(self):
        self.__origin = self.__trip.get_destination()

    def generate_service_event(self):
        event = VehicleServiceEvent(self)
        self.__event_list.append(event)
        # update currentEvent.
        self.__current_event = event

    def service_event_update(self):
        self.__trip_list.append(self.__trip)
        self.__trip = None
