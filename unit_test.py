import unittest

from description import *
from aircraft import Aircraft
from common import EventDispatcher


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
    print('Good!')
    return True


class MyTestCase(unittest.TestCase):
    def test_aircraft(self):
        self.assertEqual(True, aircraft_test())  # add assertion here


if __name__ == '__main__':
    unittest.main()
