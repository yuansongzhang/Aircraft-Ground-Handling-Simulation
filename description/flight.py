# -*- coding: utf-8 -*-
from .gate_position import GatePosition


class Flight:
    def __init__(self,
                 category,
                 scheduled_departure_time,
                 scheduled_arrival_time,
                 origin: GatePosition,
                 destination: GatePosition
                 ):
        self.__category = category  # 0 arrival flight, 1 departure flight
        self.__scheduled_departure_time = scheduled_departure_time
        self.__scheduled_arrival_time = scheduled_arrival_time
        self.__origin = origin
        self.__destination = destination
        self.__real_departure_time = None
        self.__real_arrival_time = None
        self.__server = None  # a vehicle providing ground handling service

    def set_server(self, server):
        self.__server = server

    def set_real_departure_time(self, real_departure_time):
        self.__real_departure_time = real_departure_time

    def set_real_arrival_time(self, real_arrival_time):
        self.__real_arrival_time = real_arrival_time

    def get_category(self):
        return self.__category

    def get_scheduled_departure_time(self):
        return self.__scheduled_departure_time

    def get_scheduled_arrival_time(self):
        return self.__scheduled_arrival_time

    def get_origin(self):
        return self.__origin

    def get_destination(self):
        return self.__destination

    def get_real_departure_time(self):
        return self.__real_departure_time

    def get_real_arrival_time(self):
        return self.__real_arrival_time

    def get_server(self):
        return self.__server
