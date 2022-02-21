# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

INFINITY = 10 ** 10


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

    @abstractmethod
    def get_log_info(self):
        pass


class AircraftDepartureGatePositionEvent(Event):
    def __init__(self, aircraft):
        super().__init__()
        self.__aircraft = aircraft
        self.__departure_gate_position = None
        self.__departure_timestamp = None
        self.update()

    def update(self):
        aircraft = self.__aircraft
        # todo: random travel time
        if aircraft.get_ground_handling_service_state():  # interaction with vehicles
            assert aircraft.get_ground_handling_service_finished_time() is not None
            self._triggering_timestamp = max(aircraft.get_flight().get_scheduled_departure_time(),
                                             aircraft.get_ground_handling_service_finished_time())
        else:
            self._triggering_timestamp = INFINITY
        self.__departure_gate_position = aircraft.get_flight().get_origin()
        self.__departure_timestamp = self._triggering_timestamp

    def execute(self):
        # updates aircraft.
        self.__aircraft.get_flight().set_real_departure_time(self.__departure_timestamp)
        self.__aircraft.departure_gate_position_event_update()
        # generates next event.
        self.__aircraft.generate_arrival_gate_position_event()

    def get_log_info(self):
        log_info = {
            'event_name': self.__class__.__name__,
            'triggering_timestamp': self._triggering_timestamp,
            'aircraft_id': self.__aircraft.get_id(),
            'departure_gate_position_id': self.__departure_gate_position.get_id(),
            'departure_timestamp': self.__departure_timestamp,
            'scheduled_departure_timestamp': self.__aircraft.get_flight().get_scheduled_departure_time(),
        }
        return log_info


class AircraftArrivalGatePositionEvent(Event):
    def __init__(self, aircraft):
        super().__init__()
        self.__aircraft = aircraft
        self.__arrival_gate_position = None
        self.__arrival_timestamp = None
        self.update()

    def update(self):
        aircraft = self.__aircraft
        if aircraft.get_flight().get_category() == 1:
            # all flights end with a AircraftArrivalGatePositionEvent
            self._triggering_timestamp = aircraft.get_flight().get_scheduled_departure_time()
        else:
            # interaction with vehicles
            if aircraft.get_ground_handling_service_state():
                self._triggering_timestamp = max(aircraft.get_flight().get_scheduled_arrival_time(),
                                                 aircraft.get_ground_handling_service_arrival_time())
            else:
                self._triggering_timestamp = INFINITY
            # todo: random arrival delay
            if aircraft.get_delay_state():
                self._triggering_timestamp = max(
                    aircraft.get_flight().get_scheduled_arrival_time() + aircraft.get_arrival_delay(),
                    self._triggering_timestamp)
        assert self._triggering_timestamp is not None

        self.__arrival_gate_position = aircraft.get_flight().get_destination()
        self.__arrival_timestamp = self._triggering_timestamp

    def execute(self):
        # updates aircraft.
        self.__aircraft.get_flight().set_real_arrival_time(self.__arrival_timestamp)
        self.__aircraft.arrival_gate_position_event_update()
        # ends with arrival gate position and does not generate any event.

    def get_log_info(self):
        log_info = {
            'event_name': self.__class__.__name__,
            'triggering_timestamp': self._triggering_timestamp,
            'aircraft_id': self.__aircraft.get_id(),
            'arrival_gate_position_id': self.__arrival_gate_position.get_id(),
            'arrival_timestamp': self.__arrival_timestamp,
            'scheduled_arrival_timestamp': self.__aircraft.get_flight().get_scheduled_arrival_time(),
            'delay_state': self.__aircraft.get_delay_state(),
            'delay_time': self.__aircraft.get_arrival_delay()
        }
        return log_info


'''
class AircraftArrivalDelayEvent(Event):
    def __init__(self, aircraft):
        super().__init__()
        self.__aircraft = aircraft
        self.__estimated_arrival_time = None
        self.__delay_info_release_time = None
        self.update()

    def update(self):
        aircraft = self.__aircraft
        # post delay information 30 minutes in advance
        self._triggering_timestamp = aircraft.get_flight().get_scheduled_arrival_time() + aircraft.get_arrival_delay() - 30
        self.__delay_info_release_time = self._triggering_timestamp
        self.__estimated_arrival_time = aircraft.get_flight().get_scheduled_arrival_time() + aircraft.get_arrival_delay()

    def execute(self):
        # updates aircraft.
        self.__aircraft.set_delay_state()
        self.__aircraft.arrival_gate_position_event_update()

    def get_log_info(self):
        log_info = {
            'event_name': self.__class__.__name__,
            'triggering_timestamp': self._triggering_timestamp,
            'aircraft_id': self.__aircraft.get_id(),
            'delay_info_release_time': self.__delay_info_release_time,
            'estimated_arrival_time': self.__estimated_arrival_time,
            'scheduled_arrival_timestamp': self.__aircraft.get_flight().get_scheduled_arrival_time(),
        }
        return log_info
'''


class VehicleDepartureGatePositionEvent(Event):
    def __init__(self, vehicle):
        super().__init__()
        self.__vehicle = vehicle
        self.__departure_gate_position = None
        self.__departure_timestamp = None
        self.__release_timestamp = None
        self.update()

    def update(self):
        vehicle = self.__vehicle
        self.__release_timestamp = vehicle.get_trip().get_task_release_time()
        if vehicle.get_last_trip() is None:
            self._triggering_timestamp = vehicle.get_trip().get_task_release_time()
        else:
            aircraft = vehicle.get_last_trip().get_target_aircraft()
            # interaction with aircraft
            if aircraft.get_flight().get_category() == 0:
                # the type of the last flight is arrival
                if aircraft.get_flight().get_real_arrival_time() is None:
                    self._triggering_timestamp = INFINITY
                else:
                    self._triggering_timestamp = max(vehicle.get_trip().get_task_release_time(),
                                                     aircraft.get_flight().get_real_arrival_time())
            else:
                self._triggering_timestamp = vehicle.get_trip().get_task_release_time()
        self.__departure_gate_position = vehicle.get_origin()
        self.__departure_timestamp = self._triggering_timestamp

    def execute(self):
        # updates vehicle.
        self.__vehicle.get_trip().set_departure_time(self.__departure_timestamp)
        self.__vehicle.departure_gate_position_event_update()
        # generates next event.
        self.__vehicle.generate_arrival_gate_position_event()

    def get_log_info(self):
        log_info = {
            'event_name': self.__class__.__name__,
            'triggering_timestamp': self._triggering_timestamp,
            'vehicle_id': self.__vehicle.get_id(),
            'departure_gate_position_id': self.__departure_gate_position.get_id(),
            'departure_timestamp': self.__departure_timestamp,
            'task_release_time': self.__release_timestamp
        }
        return log_info


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
        self.__vehicle.get_trip().get_target_aircraft().set_ground_handling_service_arrival_time(
            self.__arrival_timestamp)
        self.__vehicle.arrival_gate_position_event_update()
        # generates next event.
        self.__vehicle.generate_service_event()

    def get_log_info(self):
        log_info = {
            'event_name': self.__class__.__name__,
            'triggering_timestamp': self._triggering_timestamp,
            'vehicle_id': self.__vehicle.get_id(),
            'arrival_gate_position_id': self.__arrival_gate_position.get_id(),
            'arrival_timestamp': self.__arrival_timestamp,
        }
        return log_info


class VehicleServiceEvent(Event):
    def __init__(self, vehicle):
        super().__init__()
        self.__vehicle = vehicle
        self.__service_time = None
        self.update()

    def update(self):
        vehicle = self.__vehicle
        # todo: random service time
        self.__service_time = 10
        self._triggering_timestamp = vehicle.get_trip().get_arrival_time() + self.__service_time

    def execute(self):
        # updates vehicle.
        self.__vehicle.get_trip().set_service_time(self.__service_time)
        self.__vehicle.get_trip().get_target_aircraft().set_ground_handling_service_finished_time(
            self._triggering_timestamp)
        self.__vehicle.service_event_update()
        # finishes the current trip and does not generate any event.

    def get_log_info(self):
        log_info = {
            'event_name': self.__class__.__name__,
            'triggering_timestamp': self._triggering_timestamp,
            'vehicle_id': self.__vehicle.get_id(),
            'service_time': self.__service_time,
        }
        return log_info


class GroundHandlingDispatchEvent(Event):
    def __init__(self, ground_handling):
        super().__init__()
        self.__ground_handling = ground_handling
        self.__dispatch_time = None
        self.update()

    def update(self):
        ground_handling = self.__ground_handling
        self._triggering_timestamp = ground_handling.get_last_dispatch_time() + ground_handling.get_dispatch_interval()
        self.__dispatch_time = self._triggering_timestamp

    def execute(self):
        # updates ground handling.
        self.__ground_handling.set_dispatch_time(self.__dispatch_time)
        self.__ground_handling.dispatch_event_update()
        # generates next event.
        self.__ground_handling.generate_waiting_event()

    def get_log_info(self):
        log_info = {
            'event_name': self.__class__.__name__,
            'triggering_timestamp': self._triggering_timestamp,
            'dispatch_time': self.__dispatch_time,
        }
        return log_info


class GroundHandlingWaitingEvent(Event):
    def __init__(self, ground_handling):
        super().__init__()
        self.__ground_handling = ground_handling
        self.update()

    def update(self, *args, **kwargs):
        ground_handling = self.__ground_handling
        self._triggering_timestamp = ground_handling.get_dispatch_time()

    def execute(self, *args, **kwargs):
        # updates ground handling.
        self.__ground_handling.waiting_event_update()
        # generates next event.
        self.__ground_handling.generate_dispatch_event()

    def get_log_info(self):
        log_info = {
            'event_name': self.__class__.__name__,
            'triggering_timestamp': self._triggering_timestamp,
        }
        return log_info
