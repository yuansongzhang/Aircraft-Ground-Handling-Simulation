import unittest

from description import *
from aircraft import Aircraft
from common import EventDispatcher
from vehicle import Vehicle


def get_aircraft():
    virtual_gate_position = GatePosition('Virtual', 0, '001')
    gate_position1 = GatePosition('PD', 0, '001')
    gate_position2 = GatePosition('HQ', 0, '002')

    flight1 = Flight(category=0,  # Arrival
                     scheduled_departure_time=None,
                     scheduled_arrival_time=8,
                     origin=virtual_gate_position,
                     destination=gate_position1,
                     )
    aircraft1 = Aircraft(aircraft_id='MU9712', flight=flight1)

    flight2 = Flight(category=1,  # Departure
                     scheduled_departure_time=9,
                     scheduled_arrival_time=None,
                     origin=gate_position2,
                     destination=virtual_gate_position,
                     )
    aircraft2 = Aircraft(aircraft_id='MU9713', flight=flight2)
    return [aircraft1, aircraft2]


def aircraft_test():
    aircraft_list = get_aircraft()
    event_dispatcher = EventDispatcher(aircraft_list)

    while not event_dispatcher.is_finished():
        first_event = None
        for aircraft in aircraft_list:
            event = aircraft.get_current_event()
            if event is None:
                continue
            if first_event is None:
                first_event = event
            elif first_event.get_triggering_timestamp() > event.get_triggering_timestamp():
                first_event = event
        first_event.update()
        first_event.execute()
        print(first_event)
    print('Aircraft test pass.')
    return True


def vehicle_test():
    gate_position1 = GatePosition('PD', 0, '001')
    gate_position2 = GatePosition('PD', 0, '002')
    gate_position3 = GatePosition('PD', 0, '003')
    trip1 = Trip(task_release_time=6, destination=gate_position2)
    trip2 = Trip(task_release_time=6, destination=gate_position3)
    trip3 = Trip(task_release_time=6, destination=gate_position1)

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


class MyTestCase(unittest.TestCase):
    def test_aircraft(self):
        self.assertEqual(True, aircraft_test())  # add assertion here

    def test_vehicle(self):
        self.assertEqual(True, vehicle_test())  # add assertion here


if __name__ == '__main__':
    unittest.main()