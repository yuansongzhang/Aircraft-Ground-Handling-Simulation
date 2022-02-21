# -*- coding: utf-8 -*-
from common import GroundHandlingWaitingEvent
from common import GroundHandlingDispatchEvent
from .algorithm import random_match


class GroundHandling:
    def __init__(self, aircraft_list, vehicle_list):
        self.__dispatch_interval = 10
        self.__last_dispatch_time = 0
        self.__dispatch_time = None
        self.__aircraft_list = aircraft_list
        self.__vehicle_list = vehicle_list
        self.__event_list = []
        self.__current_event = None
        self.generate_dispatch_event()

    def set_dispatch_time(self, dispatch_time):
        self.__dispatch_time = dispatch_time

    def set_last_dispatch_time(self, dispatch_time):
        self.__last_dispatch_time = dispatch_time

    def get_last_dispatch_time(self):
        return self.__last_dispatch_time

    def get_dispatch_interval(self):
        return self.__dispatch_interval

    def get_dispatch_time(self):
        return self.__dispatch_time

    def get_current_event(self):
        return self.__current_event

    def generate_dispatch_event(self):
        event = GroundHandlingDispatchEvent(self)
        self.__event_list.append(event)
        # update currentEvent.
        self.__current_event = event

    def dispatch_event_update(self):
        veh_list = []
        for veh in self.__vehicle_list:
            if veh.get_trip() is None:
                veh_list.append(veh)
        aircraft_list = []
        for aircraft in self.__aircraft_list:
            if aircraft.get_flight().get_server() is None:
                aircraft_list.append(aircraft)
            elif aircraft.get_delay_state():
                # virtual arrival event
                if aircraft.get_flight().get_category() == 1:
                    continue
                estimated_arrival_time = aircraft.get_arrival_delay() + aircraft.get_flight().get_scheduled_arrival_time()
                waiting_time = estimated_arrival_time - self.__dispatch_time
                if waiting_time > 30 and (self.__dispatch_time + 60) > estimated_arrival_time:
                    aircraft_list.append(aircraft)
                    veh = aircraft.get_flight().get_server()
                    veh_list.append(veh)
                    veh.get_trip().set_cancellation()
                    veh.get_trip_list().append(veh.get_trip())
                    veh.set_trip(None)
        random_match(self.__dispatch_time, veh_list, aircraft_list)

    def generate_waiting_event(self):
        event = GroundHandlingWaitingEvent(self)
        self.__event_list.append(event)
        # update currentEvent.
        self.__current_event = event

    def waiting_event_update(self):
        self.__last_dispatch_time = self.__dispatch_time
