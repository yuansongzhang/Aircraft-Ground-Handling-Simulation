# -*- coding: utf-8 -*-
from description import *
from aircraft import Aircraft
from common import EventDispatcher
from vehicle import Vehicle
from ground_handling import GroundHandling
from utils.reader import generate_instances

import json


def get_all_instances():
    gate_position_list = []
    aircraft_list = []
    vehicle_list = []
    virtual_gate_position = GatePosition('Virtual', 0, '001')
    gate_position1 = GatePosition('PD', 0, '001')
    gate_position2 = GatePosition('PD', 0, '002')
    gate_position3 = GatePosition('PD', 0, '003')
    gate_position_list.append(gate_position1)
    gate_position_list.append(gate_position2)
    gate_position_list.append(gate_position3)

    flight1 = Flight(category=0,  # Arrival
                     scheduled_departure_time=None,
                     scheduled_arrival_time=8 * 60,
                     origin=virtual_gate_position,
                     destination=gate_position1,
                     )
    aircraft1 = Aircraft(aircraft_id='MU0001', flight=flight1)

    flight2 = Flight(category=1,  # Departure
                     scheduled_departure_time=9 * 60,
                     scheduled_arrival_time=None,
                     origin=gate_position2,
                     destination=virtual_gate_position,
                     )
    aircraft2 = Aircraft(aircraft_id='MU0002', flight=flight2)

    flight3 = Flight(category=1,  # Departure
                     scheduled_departure_time=10 * 60,
                     scheduled_arrival_time=None,
                     origin=gate_position2,
                     destination=virtual_gate_position,
                     )
    aircraft3 = Aircraft(aircraft_id='MU003', flight=flight3)

    aircraft_list.append(aircraft1)
    aircraft_list.append(aircraft2)
    aircraft_list.append(aircraft3)

    veh1 = Vehicle(gate_position1)
    veh2 = Vehicle(gate_position2)
    veh3 = Vehicle(gate_position3)

    vehicle_list.append(veh1)
    vehicle_list.append(veh2)
    vehicle_list.append(veh3)
    return gate_position_list, aircraft_list, vehicle_list


def main():
    """The unit of time is minute and simulation starts at 0 time."""
    # gate_position_list, aircraft_list, vehicle_list = get_all_instances()
    gate_position_list, aircraft_list, vehicle_list = generate_instances('./data/one_day_test_data.csv')
    ground_handling = GroundHandling(aircraft_list, vehicle_list)
    event_dispatcher = EventDispatcher(aircraft_list, vehicle_list, ground_handling)

    event_list = []
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
        event_list.append(first_event)

    with open('result.json', 'w') as f:
        info_list = []
        for event in event_list:
            info_list.append(event.get_log_info())
        json.dump(info_list, f)


if __name__ == '__main__':
    main()
