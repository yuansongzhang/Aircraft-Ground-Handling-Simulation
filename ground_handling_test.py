import unittest

from description import *
from aircraft import Aircraft
from common import EventDispatcher
from vehicle import Vehicle
from vehicle_xingli import VehicleXingli
from vehicle_jiayou import VehicleJiayou
from vehicle_baidu import VehicleBaidu
from vehicle_shipin import VehicleShipin
from vehicle_qingshui import VehicleQingshui
from vehicle_laji import VehicleLaji
from vehicle_wushui import VehicleWushui
from ground_handling import GroundHandling


        
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
    virtual_gate_position = GatePosition('Virtual', 1, '001', 5, 5)
    gate_position1 = GatePosition('PD', 0, '001', 10, 10)
    gate_position2 = GatePosition('HQ', 1, '002', 20, 20)
    gate_position3 = GatePosition('PD', 0, '001', 30, 30)
    gate_position4 = GatePosition('HQ', 1, '002', 40, 40)

    flight1 = Flight(category=0,  # Arrival
                     scheduled_departure_time=None,
                     scheduled_arrival_time=50,
                     local_gate_position=gate_position1, #近机位
                     real_departure_time=None,
                     real_arrival_time=110,
                     other_gate_position=virtual_gate_position,
                     )
    aircraft1 = Aircraft(aircraft_id='MU9712', flight=flight1, status=0)
    
    flight4 = Flight(category=0,  # Arrival
                     scheduled_departure_time=None,
                     scheduled_arrival_time=80,
                     local_gate_position=gate_position4, #远机位
                     real_departure_time=None,
                     real_arrival_time=80,
                     other_gate_position=virtual_gate_position,
                     )
    aircraft4 = Aircraft(aircraft_id='MU9715', flight=flight4, status=0)
    
    flight2 = Flight(category=1,  # Departure
                     scheduled_departure_time=115,
                     scheduled_arrival_time=None,
                     real_departure_time=115,
                     real_arrival_time=None,
                     local_gate_position=gate_position2,#远机位
                     other_gate_position=virtual_gate_position,
                     )
    aircraft2 = Aircraft(aircraft_id='MU9713', flight=flight2, status=0)
    
    flight3 = Flight(category=1,  # Departure
                     scheduled_departure_time=90,
                     scheduled_arrival_time=None,
                     real_departure_time=130,
                     real_arrival_time=None,
                     local_gate_position=gate_position3, #近机位
                     other_gate_position=virtual_gate_position,
                     )
    aircraft3 = Aircraft(aircraft_id='MU9714', flight=flight3, status=0)

    veh1 = Vehicle(name="qianyin1",v=10,x=0,y=0,aircraft=None,timestamp=0,servicestatus=0)
    veh2 = Vehicle(name="qianyin2",v=10,x=0,y=0,aircraft=None,timestamp=0,servicestatus=0)
    veh3 = VehicleXingli(name="xingli1",v=20,x=0,y=0,aircraft=None,timestamp=0,servicestatus=0)
    veh4 = VehicleXingli(name="xingli2",v=20,x=0,y=0,aircraft=None,timestamp=0,servicestatus=0)
    veh5 = VehicleJiayou(name="jiayou1",v=20,x=0,y=0,aircraft=None,timestamp=0,servicestatus=0)
    veh6 = VehicleJiayou(name="jiayou2",v=20,x=0,y=0,aircraft=None,timestamp=0,servicestatus=0)
    veh7 = VehicleBaidu(name="baidu1",v=20,x=0,y=0,aircraft=None,timestamp=0,servicestatus=0)
    veh8 = VehicleBaidu(name="baidu2",v=20,x=0,y=0,aircraft=None,timestamp=0,servicestatus=0)
    veh9 = VehicleShipin(name="shipin1",v=20,x=0,y=0,aircraft=None,timestamp=0,servicestatus=0)
    veh10 = VehicleShipin(name="shipin2",v=20,x=0,y=0,aircraft=None,timestamp=0,servicestatus=0)
    veh11 = VehicleQingshui(name="qingshui1",v=20,x=0,y=0,aircraft=None,timestamp=0,servicestatus=0)
    veh12 = VehicleQingshui(name="qingshui2",v=20,x=0,y=0,aircraft=None,timestamp=0,servicestatus=0)
    veh13 = VehicleLaji(name="laji1",v=20,x=0,y=0,aircraft=None,timestamp=0,servicestatus=0)
    veh14 = VehicleLaji(name="laji2",v=20,x=0,y=0,aircraft=None,timestamp=0,servicestatus=0)
    veh15 = VehicleWushui(name="wushui1",v=20,x=0,y=0,aircraft=None,timestamp=0,servicestatus=0)
    veh16 = VehicleWushui(name="wushui2",v=20,x=0,y=0,aircraft=None,timestamp=0,servicestatus=0)
    return [aircraft1,aircraft2,aircraft3,aircraft4], [veh1,veh2], [veh3,veh4], [veh5,veh6], [veh7,veh8], [veh9,veh10], [veh11,veh12], [veh13,veh14], [veh15,veh16]


def ground_handling_test():
    """The unit of time is minute and simulation starts at 0 time."""
    aircraft_list, vehicle_list, vehicle_xingli_list, vehicle_jiayou_list ,vehicle_baidu_list, vehicle_shipin_list, vehicle_qingshui_list, vehicle_laji_list, vehicle_wushui_list= get_aircraft_and_vehicle()
    ground_handling = GroundHandling(aircraft_list, vehicle_list, vehicle_xingli_list, vehicle_jiayou_list, vehicle_baidu_list, vehicle_shipin_list, vehicle_qingshui_list, vehicle_laji_list, vehicle_wushui_list)
    event_dispatcher = EventDispatcher(aircraft_list, vehicle_list, vehicle_xingli_list, vehicle_jiayou_list, vehicle_baidu_list, vehicle_shipin_list, vehicle_qingshui_list, vehicle_laji_list, vehicle_wushui_list, ground_handling)
    
    file_test = open("file_test.txt",mode="w") #windows和Mac写法不一样，改一下就好
    file_test.truncate(0)
    
    while not event_dispatcher.is_finished():
        first_event = None
        for aircraft in aircraft_list:
            event = aircraft.get_current_event()
            if event is None:#飞行器已完成所有事件
                continue
            event.update()#如果飞机没有延误好像update就没变化
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
        
        for veh in vehicle_xingli_list:
            event = veh.get_current_event()
            if event is None or veh.get_trip() is None:
                continue
            event.update()
            if first_event is None:
                first_event = event
            elif first_event.get_triggering_timestamp() > event.get_triggering_timestamp():
                first_event = event
        
        for veh in vehicle_laji_list:
            event = veh.get_current_event()
            if event is None or veh.get_trip() is None:
                continue
            event.update()
            if first_event is None:
                first_event = event
            elif first_event.get_triggering_timestamp() > event.get_triggering_timestamp():
                first_event = event
                
        for veh in vehicle_wushui_list:
            event = veh.get_current_event()
            if event is None or veh.get_trip() is None:
                continue
            event.update()
            if first_event is None:
                first_event = event
            elif first_event.get_triggering_timestamp() > event.get_triggering_timestamp():
                first_event = event
        
        for veh in vehicle_jiayou_list:
            event = veh.get_current_event()
            if event is None or veh.get_trip() is None:
                continue
            event.update()
            if first_event is None:
                first_event = event
            elif first_event.get_triggering_timestamp() > event.get_triggering_timestamp():
                first_event = event
                
        for veh in vehicle_baidu_list:
            event = veh.get_current_event()
            if event is None or veh.get_trip() is None:
                continue
            event.update()
            if first_event is None:
                first_event = event
            elif first_event.get_triggering_timestamp() > event.get_triggering_timestamp():
                first_event = event
        
        for veh in vehicle_shipin_list:
            event = veh.get_current_event()
            if event is None or veh.get_trip() is None:
                continue
            event.update()
            if first_event is None:
                first_event = event
            elif first_event.get_triggering_timestamp() > event.get_triggering_timestamp():
                first_event = event
        
        for veh in vehicle_qingshui_list:
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
        for veh in vehicle_wushui_list:
            print(veh.get_name(),"event完成后vehicle所在地点",veh.get_x(), veh.get_y(),"event完成后vehicle的时间戳",veh.get_timestamp())
        for veh in vehicle_laji_list:
            print(veh.get_name(),"event完成后vehicle所在地点",veh.get_x(), veh.get_y(),"event完成后vehicle的时间戳",veh.get_timestamp())
        for veh in vehicle_jiayou_list:
            print(veh.get_name(),"event完成后vehicle所在地点",veh.get_x(), veh.get_y(),"event完成后vehicle的时间戳",veh.get_timestamp())
        for veh in vehicle_xingli_list:
            print(veh.get_name(),"event完成后vehicle所在地点",veh.get_x(), veh.get_y(),"event完成后vehicle的时间戳",veh.get_timestamp())
        for veh in vehicle_shipin_list:
            print(veh.get_name(),"event完成后vehicle所在地点",veh.get_x(), veh.get_y(),"event完成后vehicle的时间戳",veh.get_timestamp())
        for veh in vehicle_qingshui_list:
            print(veh.get_name(),"event完成后vehicle所在地点",veh.get_x(), veh.get_y(),"event完成后vehicle的时间戳",veh.get_timestamp())
        for veh in vehicle_baidu_list:
            print(veh.get_name(),"event完成后vehicle所在地点",veh.get_x(), veh.get_y(),"event完成后vehicle的时间戳",veh.get_timestamp())
        for veh in vehicle_list:
            print(veh.get_name(),"event完成后vehicle所在地点",veh.get_x(), veh.get_y(),"event完成后vehicle的时间戳",veh.get_timestamp())
            #print(veh.get_name(),"event完成后vehicle的时间戳",veh.get_timestamp())
        print("---------------------------------------------------------------------")
        
        file_test.write(str(first_event)+'\n'+"event触发时间"+str(first_event.get_triggering_timestamp())+'\n')
        for veh in vehicle_wushui_list:
            file_test.write(str(veh.get_name())+" event完成后vehicle所在地点 "+str(veh.get_x())+str(veh.get_y())+" event完成后vehicle的时间戳 "+str(veh.get_timestamp())+' 状态 '+str(veh.get_servicestatus())+'\n')
        for veh in vehicle_laji_list:
            file_test.write(str(veh.get_name())+" event完成后vehicle所在地点 "+str(veh.get_x())+str(veh.get_y())+" event完成后vehicle的时间戳 "+str(veh.get_timestamp())+' 状态 '+str(veh.get_servicestatus())+'\n')
        for veh in vehicle_jiayou_list:
            file_test.write(str(veh.get_name())+" event完成后vehicle所在地点 "+str(veh.get_x())+str(veh.get_y())+" event完成后vehicle的时间戳 "+str(veh.get_timestamp())+' 状态 '+str(veh.get_servicestatus())+'\n')
        for veh in vehicle_xingli_list:
            file_test.write(str(veh.get_name())+" event完成后vehicle所在地点 "+str(veh.get_x())+str(veh.get_y())+" event完成后vehicle的时间戳 "+str(veh.get_timestamp())+' 状态 '+str(veh.get_servicestatus())+'\n')
        for veh in vehicle_shipin_list:
            file_test.write(str(veh.get_name())+" event完成后vehicle所在地点 "+str(veh.get_x())+str(veh.get_y())+" event完成后vehicle的时间戳 "+str(veh.get_timestamp())+' 状态 '+str(veh.get_servicestatus())+'\n')
        for veh in vehicle_qingshui_list:
            file_test.write(str(veh.get_name())+" event完成后vehicle所在地点 "+str(veh.get_x())+str(veh.get_y())+" event完成后vehicle的时间戳 "+str(veh.get_timestamp())+' 状态 '+str(veh.get_servicestatus())+'\n')
        for veh in vehicle_baidu_list:
            file_test.write(str(veh.get_name())+" event完成后vehicle所在地点 "+str(veh.get_x())+str(veh.get_y())+" event完成后vehicle的时间戳 "+str(veh.get_timestamp())+' 状态 '+str(veh.get_servicestatus())+'\n')
        for veh in vehicle_list:
            file_test.write(str(veh.get_name())+" event完成后vehicle所在地点 "+str(veh.get_x())+str(veh.get_y())+" event完成后vehicle的时间戳 "+str(veh.get_timestamp())+' 状态 '+str(veh.get_servicestatus())+'\n')
        for air in aircraft_list:
            file_test.write(str(air.get_aircraft_id())+"  "+str(air.get_wushui_status())+str(air.get_laji_status())+str(air.get_jiayou_status())+str(air.get_xingli_status())+str(air.get_shipin_status())+str(air.get_qingshui_status())+str(air.get_baidu_status())+str(air.get_qianyin_status())+'\n')
        file_test.write("---------------------------------------------------------------------\n")
        
    file_test.close()
        
    print('Ground handling test pass.')
    return True

"""
class MyTestCase(unittest.TestCase):
    def test_aircraft(self):
        self.assertEqual(True, aircraft_test())

    def test_vehicle(self):
        self.assertEqual(True, vehicle_test())

    def test_ground_handling(self):
        self.assertEqual(True, ground_handling_test())


if __name__ == '__main__':
    unittest.main()
"""

ground_handling_test()

