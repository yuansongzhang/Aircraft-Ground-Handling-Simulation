# -*- coding: utf-8 -*-
from description import Trip


def random_match(task_release_time, vehicle_list: list, aircraft_list: list):
    veh_list = vehicle_list.copy()
    air_list = aircraft_list.copy()
    for aircraft in air_list:
        for vehicle in veh_list:
            if vehicle.get_trip() is not None:
                continue
            if aircraft.get_flight().get_category() == 1:
                new_trip = Trip(task_release_time=task_release_time,
                                destination=aircraft.get_flight().get_origin())
            else:
                new_trip = Trip(task_release_time=task_release_time,
                                destination=aircraft.get_flight().get_destination())
            vehicle.set_trip(new_trip)
            vehicle.generate_departure_gate_position_event()
            aircraft.get_flight().set_server(server=vehicle)
            break
