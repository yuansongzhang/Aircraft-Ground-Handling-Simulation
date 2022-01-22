# -*- coding: utf-8 -*-
import numpy as np
from description import Trip

# '''
def distance_match(dispatch_timestamp, vehicle_list: list, aircraft_list: list):#调度时间
    best_vehicle = None
    veh_list = vehicle_list.copy()
    air_list = aircraft_list.copy()#所有当前已知需要服务航班要按时间排序(40min内)
    print('veh_list',[veh.get_name() for veh in veh_list])
    print('air_list',[air.get_aircraft_id() for air in air_list])
    
    for aircraft in air_list:
        min_distance = 1000000
        if aircraft.get_flight().get_category() == 1:#离港
            task_release_timestamp = aircraft.get_flight().get_scheduled_departure_timestamp() - 4*10#下达的任务时间根据不同车情况不同
        else:
            task_release_timestamp = aircraft.get_flight().get_scheduled_arrival_timestamp() - 1*10
        
        if dispatch_timestamp > task_release_timestamp:#任务下达时间一定是≥调度时间
            task_release_timestamp = dispatch_timestamp

        new_trip = Trip(task_release_timestamp=task_release_timestamp,
                        destination_x=aircraft.get_flight().get_local_gate_position().get_x(),
                        destination_y=aircraft.get_flight().get_local_gate_position().get_y())
        
        for vehicle in veh_list:
            if vehicle.get_trip() is not None:
                continue
            distance = np.sqrt(np.square(vehicle.get_x()-new_trip.get_destination_x())+np.square(vehicle.get_y()-new_trip.get_destination_y()))
            if distance < min_distance:
                min_distance = distance
                best_vehicle = vehicle
        if best_vehicle == None:
            print("没有车辆")
            break
        best_vehicle.set_trip(new_trip)
        best_vehicle.set_aircraft(aircraft)
        best_vehicle.generate_departure_gate_position_event()
        aircraft.set_status(2)
        # aircraft.get_flight().set_server(server=best_vehicle)
       # break
    

 

'''
def random_match(dispatch_timestamp, vehicle_list: list, aircraft_list: list):
    veh_list = vehicle_list.copy()
    air_list = aircraft_list.copy()
    for aircraft in air_list:
        if aircraft.get_flight().get_category() == 1:#离港
            task_release_timestamp = aircraft.get_flight().get_scheduled_departure_timestamp() - 4*10#下达的任务时间根据不同车情况不同
        else:
            task_release_timestamp = aircraft.get_flight().get_scheduled_arrival_timestamp() - 1*10
        
        if dispatch_timestamp > task_release_timestamp:#任务下达时间一定是≥调度时间
            task_release_timestamp = dispatch_timestamp

        new_trip = Trip(task_release_timestamp=task_release_timestamp,
                        destination_x=aircraft.get_flight().get_local_gate_position().get_x(),
                        destination_y=aircraft.get_flight().get_local_gate_position().get_y())
        for vehicle in veh_list:
            if vehicle.get_trip() is not None:
                continue
            vehicle.set_trip(new_trip)
            vehicle.set_aircraft(aircraft)
            vehicle.generate_departure_gate_position_event()
            aircraft.set_status(2)
            break#一旦匹配到空闲车辆就不再寻找车辆（从车辆中循环跳出），开始下一个aircraft循环
'''
