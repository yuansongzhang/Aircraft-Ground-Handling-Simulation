# -*- coding: utf-8 -*-
from description import Flight
from common import *


class Aircraft:
    def __init__(self,
                 aircraft_id,
                 flight: Flight,
                 arrival_delay
                 ):
        self.__aircraft_id = aircraft_id
        self.__flight = flight
        self.__event_list = list()
        self.__current_event = None
        # departure
        self.__ground_handling_service_state = False
        self.__ground_handling_service_finished_time = None
        self.__ground_handling_service_arrival_time = None
        self.__delay_state = True
        # post delay info 30 min in advance
        self.__arrival_delay_release_time = 30
        self.__arrival_delay = arrival_delay

        if self.__flight.get_category() == 1:
            self.generate_departure_gate_position_event()
        elif self.__flight.get_category() == 0:
            self.generate_arrival_gate_position_event()

    def get_delay_state(self):
        return self.__delay_state

    def get_arrival_delay(self):
        return self.__arrival_delay

    def get_ground_handling_service_arrival_time(self):
        return self.__ground_handling_service_arrival_time

    def set_ground_handling_service_arrival_time(self, arrival_time):
        self.__ground_handling_service_arrival_time = arrival_time

    def set_ground_handling_service_finished_time(self, finished_time):
        self.__ground_handling_service_finished_time = finished_time

    def set_ground_handling_service_state(self):
        self.__ground_handling_service_state = True

    def get_ground_handling_service_finished_time(self):
        return self.__ground_handling_service_finished_time

    def get_ground_handling_service_state(self):
        return self.__ground_handling_service_state

    def get_id(self):
        return self.__aircraft_id

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

    def departure_gate_position_event_update(self):
        pass

    def generate_arrival_gate_position_event(self):
        event = AircraftArrivalGatePositionEvent(self)
        self.__event_list.append(event)
        # update currentEvent.
        self.__current_event = event

    def arrival_gate_position_event_update(self):
        self.__current_event = None

    def arrival_delay_event_update(self):
        pass
