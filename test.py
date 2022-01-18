#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 20:56:52 2022

@author: duidui
"""

import unittest
from description import *
from aircraft.aircraft import Aircraft
from common import EventDispatcher
from vehicle import Vehicle
#from ground_handling import GroundHandling
"""
def get_aircraft_and_vehicle():
    virtual_gate_position = GatePosition('Virtual', 0, '001', 10, 10)
    gate_position1 = GatePosition('PD', 0, '001', 10, 10)
    gate_position2 = GatePosition('HQ', 0, '002', 10, 10)

    flight1 = Flight(category=0,  # Arrival
                     scheduled_departure_time=None,
                     scheduled_arrival_time=8 * 60,
                     local_gate_position=virtual_gate_position,
                     other_gate_position=gate_position1,
                     )
    aircraft1 = Aircraft(aircraft_id='MU9712', flight=flight1, status=0)

    flight2 = Flight(category=1,  # Departure
                     scheduled_departure_time=9 * 60,
                     scheduled_arrival_time=None,
                     local_gate_position=virtual_gate_position,
                     other_gate_position=gate_position2,
                     )
    aircraft2 = Aircraft(aircraft_id='MU9713', flight=flight2, status=0)

    veh1 = Vehicle(name="qianyin",v=10,x=1,y=1,aircraft=0,timestamp=0,servicestatus=0,
                 preparationtime=10,servicetime=10)
    veh2 = Vehicle(name="qianyin",v=10,x=2,y=2,aircraft=0,timestamp=0,servicestatus=0,
                 preparationtime=10,servicetime=10)
    return [aircraft1, aircraft2], [veh1, veh2]
"""

# def get_aircraft():
#     virtual_gate_position = GatePosition('Virtual', 0, '001', 10, 10)
#     gate_position1 = GatePosition('PD', 0, '001', 10, 10)
#     gate_position2 = GatePosition('HQ', 0, '002', 10, 10)

#     flight1 = Flight(category=0,  # Arrival
#                      scheduled_departure_time=None,
#                      scheduled_arrival_time=8 * 60,
#                      local_gate_position=virtual_gate_position,
#                      other_gate_position=gate_position1,
#                      )
#     aircraft1 = Aircraft(aircraft_id='MU9712', flight=flight1, status=0)

#     flight2 = Flight(category=1,  # Departure
#                      scheduled_departure_time=9 * 60,
#                      scheduled_arrival_time=None,
#                      local_gate_position=virtual_gate_position,
#                      other_gate_position=gate_position2,
#                      )
#     aircraft2 = Aircraft(aircraft_id='MU9713', flight=flight2, status=0)
#     return [aircraft1, aircraft2]

"""
def aircraft_test():
    aircraft_list = get_aircraft()
    for aircraft in aircraft_list:
        print(aircraft.get_aircraft_id())
"""
def aircraft_test():
    aircraft_list = get_aircraft()
    event_dispatcher = EventDispatcher(aircraft_list)

    while not event_dispatcher.is_finished():
        first_event = None
        for aircraft in aircraft_list: #获取时间戳最先的aircraft
            event = aircraft.get_current_event()
            if event is None:
                continue
            if first_event is None:
                first_event = event #firstevent上一个aircraft的事件
            elif first_event.get_triggering_timestamp() > event.get_triggering_timestamp():
                first_event = event
        first_event.update()
        first_event.execute()
        print(first_event)
    print('Aircraft test pass.')
    return True
        
        
def vehicle_test():
    virtual_gate_position = GatePosition('Virtual', 0, '001', 10, 10)
    gate_position1 = GatePosition('PD', 0, '001', 10, 10)
    gate_position2 = GatePosition('HQ', 0, '002', 10, 10)

    flight1 = Flight(category=0,  # Arrival
                     scheduled_departure_time=None,
                     scheduled_arrival_time=8 * 60,
                     local_gate_position=virtual_gate_position,
                     other_gate_position=gate_position1,
                     )
    aircraft1 = Aircraft(aircraft_id='MU9712', flight=flight1, status=0)
    
    vehicle1 = Vehicle(name="qianyin",v=10,x=1,y=1,aircraft=aircraft1,timestamp=0,servicestatus=0,
                 preparationtime=10,servicetime=10)
    
   
    
    veh = Vehicle(gate_position1)
    for trip in [trip1, trip2, trip3]:
        print(veh.get_origin().get_id())
        # assigns trips
        veh.set_trip(trip)
        veh.generate_departure_gate_position_event()
        while veh.get_trip() is not None:
            event = veh.get_current_event()
            event.update()
            event.execute()
            print(event)
        print(veh.get_origin().get_id())
    print('Vehicle test pass.')
    return True


flight1 = Flight()
print(flight1.get_category())
print(flight1.get_scheduled_departure_time())
