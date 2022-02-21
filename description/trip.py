# -*- coding: utf-8 -*-
from .gate_position import GatePosition
from aircraft import Aircraft


class Trip:
    """The instance of Trip class is produced by GroundHandling class."""

    def __init__(self,
                 task_release_time,
                 destination: GatePosition,
                 target_aircraft: Aircraft,
                 ):
        self.__task_release_time = task_release_time
        self.__destination = destination
        self.__departure_time = None  # the time to depart from the current gate position of the vehicle
        self.__arrival_time = None  # the time to arrive at the gate position of the target aircraft
        self.__service_time = None
        self.__target_aircraft = target_aircraft
        # a trip can be canceled due to the arrival delay of the target aircraft
        self.__cancellation = False

    def set_cancellation(self):
        self.__cancellation = True

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

    def get_target_aircraft(self):
        return self.__target_aircraft

    def get_cancellation(self):
        return self.__cancellation

    def get_log_info(self):
        log_info = {
            'event_name': self.__class__.__name__,
            'task_release_time': self.__task_release_time,
            'destination': self.__destination.get_id(),
            'target_aircraft': self.__target_aircraft.get_id(),
            'aircraft_scheduled_arrival_time': self.__target_aircraft.get_flight().get_scheduled_arrival_time(),
            'aircraft_scheduled_departure_time': self.__target_aircraft.get_flight().get_scheduled_departure_time(),
            'departure_time': self.__departure_time,
            'arrival_timestamp': self.__arrival_time,
            'service_time': self.__service_time
        }
        return log_info
