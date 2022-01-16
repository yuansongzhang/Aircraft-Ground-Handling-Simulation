# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Event:
    __meta_class__ = ABCMeta

    def __init__(self):
        self._triggering_timestamp = None

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    def get_triggering_timestamp(self):
        return self._triggering_timestamp


class AircraftDepartureGatePositionEvent(Event):
    def __init__(self, aircraft):
        super().__init__()
        self.__aircraft = aircraft
        self.__departure_gate_position = None
        self.__departure_timestamp = None
        self.update()

    def update(self):
        aircraft = self.__aircraft
        # todo: interaction with vehicles, random travel time
        self._triggering_timestamp = aircraft.get_flight().get_scheduled_departure_time()
        self.__departure_gate_position = aircraft.get_flight().get_origin()
        self.__departure_timestamp = self._triggering_timestamp

    def execute(self):
        # updates aircraft.
        self.__aircraft.get_flight().set_real_departure_time(self.__departure_timestamp)
        self.__aircraft.departure_gate_position_event_update()
        # generates next event.
        self.__aircraft.generate_arrival_gate_position_event()


class AircraftArrivalGatePositionEvent(Event):
    def __init__(self, aircraft):
        super().__init__()
        self.__aircraft = aircraft
        self.__arrival_gate_position = None
        self.__arrival_timestamp = None
        self.update()

    def update(self):
        aircraft = self.__aircraft
        # todo: interaction with vehicles
        self._triggering_timestamp = aircraft.get_flight().get_scheduled_arrival_time()
        self.__arrival_gate_position = aircraft.get_flight().get_destination()
        self.__arrival_timestamp = self._triggering_timestamp

    def execute(self):
        # updates aircraft.
        self.__aircraft.get_flight().set_real_arrival_time(self.__arrival_timestamp)
        self.__aircraft.arrival_gate_position_event_update()
        # ends with arrival gate position and does not generate any event.


class VehicleDepartureGatePositionEvent(Event):
    def __init__(self, vehicle):
        super().__init__()
        self.__vehicle = vehicle
        self.__departure_gate_position = None
        self.__departure_timestamp = None
        self.update()

    def update(self):
        vehicle = self.__vehicle
        # todo: interaction with aircraft
        self._triggering_timestamp = vehicle.get_trip().get_task_release_time()
        self.__departure_gate_position = vehicle.get_origin()
        self.__departure_timestamp = self._triggering_timestamp

    def execute(self):
        # updates vehicle.
        self.__vehicle.get_trip().set_departure_time(self.__departure_timestamp)
        self.__vehicle.departure_gate_position_event_update()
        # generates next event.
        self.__vehicle.generate_arrival_gate_position_event()


class VehicleArrivalGatePositionEvent(Event):
    def __init__(self, vehicle):
        super().__init__()
        self.__vehicle = vehicle
        self.__arrival_gate_position = None
        self.__arrival_timestamp = None
        self.update()

    def update(self):
        vehicle = self.__vehicle
        # todo: random trip time, interaction with aircraft
        self._triggering_timestamp = vehicle.get_trip().get_departure_time() + 10
        self.__arrival_gate_position = vehicle.get_trip().get_destination()
        self.__arrival_timestamp = self._triggering_timestamp

    def execute(self):
        # updates vehicle.
        self.__vehicle.get_trip().set_arrival_time(self.__arrival_timestamp)
        self.__vehicle.arrival_gate_position_event_update()
        # generates next event.
        self.__vehicle.generate_service_event()


class VehicleServiceEvent(Event):
    def __init__(self, vehicle):
        super().__init__()
        self.__vehicle = vehicle
        self.__service_time = None
        self.update()

    def update(self):
        vehicle = self.__vehicle
        self._triggering_timestamp = vehicle.get_trip().get_arrival_time()
        # todo: random service time
        self.__service_time = 10

    def execute(self):
        # updates vehicle.
        self.__vehicle.get_trip().set_service_time(self.__service_time)
        self.__vehicle.service_event_update()
        # finishes the current trip and does not generate any event.


class GroundHandlingDispatchEvent(Event):
    def __init__(self):
        super().__init__()

    def update(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        pass


class GroundHandlingWaitingEvent(Event):
    def __init__(self):
        super().__init__()

    def update(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        pass
