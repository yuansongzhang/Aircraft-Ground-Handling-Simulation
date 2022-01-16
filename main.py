# -*- coding: utf-8 -*-
from description import *
from aircraft import Aircraft
from common import EventDispatcher
from vehicle import Vehicle
from ground_handling import GroundHandling


def get_aircraft_and_vehicle():
    virtual_gate_position = GatePosition('Virtual', 0, '001')
    gate_position1 = GatePosition('PD', 0, '001')
    gate_position2 = GatePosition('HQ', 0, '002')

    flight1 = Flight(category=0,  # Arrival
                     scheduled_departure_time=None,
                     scheduled_arrival_time=8 * 60,
                     origin=virtual_gate_position,
                     destination=gate_position1,
                     )
    aircraft1 = Aircraft(aircraft_id='MU9712', flight=flight1)

    flight2 = Flight(category=1,  # Departure
                     scheduled_departure_time=9 * 60,
                     scheduled_arrival_time=None,
                     origin=gate_position2,
                     destination=virtual_gate_position,
                     )
    aircraft2 = Aircraft(aircraft_id='MU9713', flight=flight2)

    veh1 = Vehicle(gate_position1)
    veh2 = Vehicle(gate_position2)
    return [aircraft1, aircraft2], [veh1, veh2]


def main():
    """The unit of time is minute and simulation starts at 0 time."""
    aircraft_list, vehicle_list = get_aircraft_and_vehicle()
    ground_handling = GroundHandling(aircraft_list, vehicle_list)
    event_dispatcher = EventDispatcher(aircraft_list, vehicle_list, ground_handling)

    while not event_dispatcher.is_finished():
        first_event = None
        for aircraft in aircraft_list:
            event = aircraft.get_current_event()
            if event is None:
                continue
            event.update()
            if first_event is None:
                first_event = event
            elif first_event.get_triggering_timestamp() > event.get_triggering_timestamp():
                first_event = event

        for veh in vehicle_list:
            event = veh.get_current_event()
            if event is None or veh.get_trip() is None:
                continue
            event.update()
            if first_event is None:
                first_event = event
            elif first_event.get_triggering_timestamp() > event.get_triggering_timestamp():
                first_event = event

        event = ground_handling.get_current_event()
        if event is None:
            continue
        event.update()
        if first_event is None:
            first_event = event
        elif first_event.get_triggering_timestamp() > event.get_triggering_timestamp():
            first_event = event

        first_event.update()
        first_event.execute()
        print(first_event)
    print('Ground handling test pass.')


if __name__ == '__main__':
    main()
