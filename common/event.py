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
        self.__aircraft.aircraft_departure_gate_position_event_update()
        # generates next event.
        self.__aircraft.generate_arrival_gate_position_event()


class AircraftArrivalGatePositionEvent(Event):
    def __init__(self, aircraft):
        super().__init__()
        self.__aircraft = aircraft
        self.__arrival_gate_position = None
        self.__arrival_timestamp = None
        self.__last_arrival_timestamp = None
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
        self.__aircraft.aircraft_arrival_gate_position_event_update()
        # ends with arrival gate position and does not generate any event.


class VehicleArrivalGatePositionEvent(Event):
    "到达事件"

    def __init__(self, vehicle1, sessionStartTimestamp, ArrivalGatePositionTimestamp):
        self.vehicle1 = vehicle1
        self.sessionStartTimestamp = sessionStartTimestamp
        self.ArrivalGatePositionTimestamp = ArrivalGatePositionTimestamp  # 到达机位时间戳如何给？

    def update(self):
        self.sessionStartTimestamp = self.vehicle1.Time  # 开始时间
        self.triggeringTimestamp = self.sessionStartTimestamp
        self.vehicle1.run()

    def execute(self):
        self.ArrivalGatePositionTimestamp += self.vehicle1.PreprationTime


class VehicleDepartureGatePositionEvent(Event):
    "驶离事件"

    def __init__(self, vehicle1, departureTimestamp):
        self.vehicle1 = vehicle1
        self.departureTimestamp = departureTimestamp

    def update(self):
        self.departureTimestamp = VehicleServiceEvent.serviceFinishTimestamp

    def execute(self):
        pass


class VehicleServiceEvent(Event):
    "服务事件"

    def __init__(self, vehicle1, aircraft, serviceStartTimestamp, serviceFinishTimestamp):
        self.vehicle1 = vehicle1
        self.aircraft = aircraft
        self.serviceStartTimestamp = serviceStartTimestamp
        self.serviceFinishTimestamp = serviceFinishTimestamp

    def update(self):
        self.serviceStartTimestamp = self.aircraft.getNextGatePositionArrivalTimestamp()
        self.triggeringTimestamp = self.serviceStartTimestamp

    def execute(self):
        self.vehicle1.finish()
        self.serviceFinishTimestamp = self.serviceStartTimestamp + self.vehicle1.ServiceTime()


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
