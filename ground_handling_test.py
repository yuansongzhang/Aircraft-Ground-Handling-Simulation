import unittest

from description import *
from aircraft import Aircraft
from common import EventDispatcher
from vehicle import Vehicle
from ground_handling import GroundHandling
from utils import reader

def get_aircraft():
    virtual_gate_position = GatePosition('Virtual', 0, '001', 10, 10)
    gate_position1 = GatePosition('PD', 0, '001', 10, 10)
    gate_position2 = GatePosition('HQ', 0, '002', 10, 10)

    flight1 = Flight(category=0,  # Arrival
                     scheduled_departure_time=None,
                     scheduled_arrival_time=8 * 60,
                     real_departure_time=None,
                     real_arrival_time=8*60,
                     local_gate_position=virtual_gate_position,
                     other_gate_position=gate_position1,
                     )
    aircraft1 = Aircraft(aircraft_id='MU9712', flight=flight1, status=0)

    flight2 = Flight(category=1,  # Departure
                     scheduled_departure_time=9 * 60,
                     scheduled_arrival_time=None,
                     real_departure_time=9*60,
                     real_arrival_time=None,
                     local_gate_position=virtual_gate_position,
                     other_gate_position=gate_position2,
                     )
    aircraft2 = Aircraft(aircraft_id='MU9713', flight=flight2, status=0)
    return [aircraft1, aircraft2]

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
    virtual_gate_position = GatePosition('Virtual', 0, '001', 5, 5)
    gate_position1 = GatePosition('PD', 0, '001', 10, 10)
    gate_position2 = GatePosition('HQ', 0, '002', 20, 20)

    flight1 = Flight(category=0,  # Arrival
                     scheduled_departure_time=None,
                     scheduled_arrival_time=8 * 10,
                     real_departure_time=None,
                     real_arrival_time=80,
                     local_gate_position=gate_position1,
                     other_gate_position=virtual_gate_position,
                     )
    aircraft1 = Aircraft(aircraft_id='MU9712', flight=flight1, status=0)
    
    flight2 = Flight(category=1,  # Departure
                     scheduled_departure_time=11 * 10,
                     scheduled_arrival_time=None,
                     real_departure_time=None,
                     real_arrival_time=11*10,
                     local_gate_position=gate_position2,
                     other_gate_position=virtual_gate_position,
                     )
    aircraft2 = Aircraft(aircraft_id='MU9713', flight=flight2, status=0)
    
    
    vehicle1 = Vehicle(name="qianyin",v=10,x=1,y=1,aircraft=None,timestamp=0,servicestatus=0)
    vehicle2 = Vehicle(name="qianyin",v=10,x=1,y=1,aircraft=None,timestamp=0,servicestatus=0)
    vehicle1.set_aircraft(aircraft1)
    vehicle2.set_aircraft(aircraft2)
    vehicle_list = [vehicle1,vehicle2]
    
    trip1 = Trip(task_release_time=6, destination_x=10, destination_y=10)
    trip2 = Trip(task_release_time=6, destination_x=20, destination_y=20)

    #veh = Vehicle(gate_position1)
    for trip in [trip1]:
        print(vehicle1.get_x(), vehicle1.get_y()) #veh起点在001
        # assigns trips
        vehicle1.set_trip(trip) #要执行去gateposition2的事件
        vehicle1.generate_departure_gate_position_event() #生成veh离开起点001
        while vehicle1.get_trip() is not None: #此时trip是veh从001去2
            event = vehicle1.get_current_event() #此时是VehicleDepartureGatePositionEvent
            event.update()
            event.execute()
            print(event)
            print("event触发时间",event.get_triggering_timestamp())
            print("event完成后vehicle所在地点",vehicle1.get_x(), vehicle1.get_y())
            print("event完成后vehicle的时间戳",vehicle1.get_timestamp())
            print("event完成后vehicle状态",vehicle1.get_servicestatus())
            print("---------------------------")
        print(vehicle1.get_x(), vehicle1.get_y())
    print('Vehicle test pass.')
    return True


def get_aircraft_and_vehicle():
    # virtual_gate_position = GatePosition('Virtual', 0, '001', 5, 5)
    # gate_position1 = GatePosition('PD', 0, '001', 10, 10)
    # gate_position2 = GatePosition('HQ', 0, '002', 20, 20)

    # flight1 = Flight(category=0,  # Arrival
    #                   scheduled_departure_timestamp=None,
    #                   scheduled_arrival_timestamp=8 * 10,
    #                   local_gate_position=gate_position1,
    #                   real_departure_timestamp=None,
    #                   real_arrival_timestamp=80,
    #                   other_gate_position=virtual_gate_position,
    #                   )
    # aircraft1 = Aircraft(aircraft_id='MU9712', flight=flight1, status=0)
    
    # flight2 = Flight(category=1,  # Departure
    #                   scheduled_departure_timestamp=50,
    #                   scheduled_arrival_timestamp=None,
    #                   real_departure_timestamp=200,
    #                   real_arrival_timestamp=None,
    #                   local_gate_position=gate_position2,
    #                   other_gate_position=virtual_gate_position,
    #                   )
    # aircraft2 = Aircraft(aircraft_id='MU9713', flight=flight2, status=0)
    
    flight1 = reader.generate_flights(r".\resources\单个航班test.xlsx")
    aircraft1 = Aircraft(aircraft_id=flight1.get_id(), flight=flight1, status=0)
    
    flight2 = reader.generate_flights(r".\resources\单个航班test.xlsx")
    aircraft2 = Aircraft(aircraft_id=flight2.get_id(), flight=flight2, status=0)
    
    veh1 = Vehicle(name="qianyin1",v=10,x=1,y=1,aircraft=None,timestamp=0,servicestatus=0)
    veh2 = Vehicle(name="qianyin2",v=10,x=1,y=1,aircraft=None,timestamp=0,servicestatus=0)
    return [aircraft1, aircraft2], [veh1, veh2]


def ground_handling_test():
    """The unit of time is minute and simulation starts at 0 time."""
    aircraft_list, vehicle_list = get_aircraft_and_vehicle()
    ground_handling = GroundHandling(aircraft_list, vehicle_list)
    event_dispatcher = EventDispatcher(aircraft_list, vehicle_list, ground_handling)

    while not event_dispatcher.is_finished():
        first_event = None
        for aircraft in aircraft_list:
            event = aircraft.get_current_event()
            if event is None:#飞行器已完成所有事件
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
        print("event触发时间",first_event.get_triggering_timestamp())
        for veh in vehicle_list:
            print(veh.get_name(),"event完成后vehicle所在地点",veh.get_x(), veh.get_y())
            print(veh.get_name(),"event完成后vehicle的时间戳",veh.get_timestamp())
            #print(veh.get_name(),"event完成后vehicle状态",veh.get_servicestatus())
        print("---------------------------")
    print('Ground handling test pass.')
    return True


class MyTestCase(unittest.TestCase):
    # def test_aircraft(self):
    #     self.assertEqual(True, aircraft_test())

    # def test_vehicle(self):
    #     self.assertEqual(True, vehicle_test())

    def test_ground_handling(self):
        self.assertEqual(True, ground_handling_test())

# """
if __name__ == '__main__':
    unittest.main()
"""

ground_handling_test()

"""