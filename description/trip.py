# -*- coding: utf-8 -*-
from .gate_position import GatePosition


class Trip:
    """The instance of Trip class is produced by GroundHandling class."""

    def __init__(self,
                 task_release_time,
                 destination: GatePosition,
                 ):
        self.__task_release_time = task_release_time
        self.__destination = destination
        self.__departure_time = None
        self.__arrival_time = None
        self.__service_time = None

    def set_arrival_time(self, arrival_time):
        self.__arrival_time = arrival_time

    def set_departure_time(self, departure_time):
        self.__departure_time = departure_time

    def set_service_time(self, service_time):
        self.__service_time = service_time

    def get_task_release_time(self):
        return self.__task_release_time

    def get_destination(self):
        return self.__destination

    def get_departure_time(self):
        return self.__departure_time

    def get_arrival_time(self):
        return self.__arrival_time
