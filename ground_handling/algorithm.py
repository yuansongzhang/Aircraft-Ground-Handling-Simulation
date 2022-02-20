# -*- coding: utf-8 -*-
import numpy as np
from description import Trip

def random_match(dispatch_time, vehicle_wushui_list:list, vehicle_laji_list:list, vehicle_qingshui_list:list, vehicle_shipin_list:list, vehicle_baidu_list:list, vehicle_jiayou_list:list, vehicle_xingli_list:list, vehicle_list: list, aircraft_list: list):#调度时间
    best_vehicle = None
    veh_wushui_list = vehicle_wushui_list.copy()
    veh_laji_list = vehicle_laji_list.copy()
    veh_qingshui_list = vehicle_qingshui_list.copy()
    veh_shipin_list = vehicle_shipin_list.copy()
    veh_baidu_list = vehicle_baidu_list.copy()
    veh_jiayou_list = vehicle_jiayou_list.copy()
    veh_xingli_list = vehicle_xingli_list.copy()
    veh_list = vehicle_list.copy()
    air_list = aircraft_list.copy()#所有当前已知需要服务航班要按时间排序(40min内)
    
    print('vehicle_wushui_list',[veh.get_name() for veh in veh_wushui_list])
    print('vehicle_laji_list',[veh.get_name() for veh in veh_laji_list])
    print('vehicle_jiayou_list',[veh.get_name() for veh in veh_jiayou_list])
    print('vehicle_xingli_list',[veh.get_name() for veh in veh_xingli_list])
    print('vehicle_shipin_list',[veh.get_name() for veh in veh_shipin_list])
    print('vehicle_qingshui_list',[veh.get_name() for veh in veh_qingshui_list])
    print('vehicle_baidu_list',[veh.get_name() for veh in veh_baidu_list])
    print('veh_list',[veh.get_name() for veh in veh_list])
    print('air_list',[air.get_aircraft_id() for air in air_list])
    
    for aircraft in air_list:
        if aircraft.get_flight().get_category() == 1:#离港
          if (aircraft.get_baidu_status()==1)&(dispatch_time>=aircraft.get_flight().get_scheduled_departure_time()-40):
              best_vehicle = None
              for vehicle in veh_baidu_list:
                  if vehicle.get_trip() is not None:
                      continue
                  best_vehicle = vehicle
                  task_release_time = aircraft.get_flight().get_scheduled_departure_time()-40
                  if dispatch_time > task_release_time:#任务下达时间一定是≥调度时间
                      task_release_time = dispatch_time
                  new_trip = Trip(task_release_time=task_release_time,
                                  destination_x=aircraft.get_flight().get_local_gate_position().get_x(),
                                  destination_y=aircraft.get_flight().get_local_gate_position().get_y())
              if best_vehicle == None:
                  print("没有车辆")
                  break
              best_vehicle.set_trip(new_trip)
              best_vehicle.set_aircraft(aircraft)
              best_vehicle.generate_departure_gate_position_event()
              aircraft.set_status(2)
              aircraft.set_baidu_status(2)
              
        else:
          if (aircraft.get_baidu_status()==1)&(dispatch_time>=aircraft.get_flight().get_scheduled_arrival_time()+5):
              best_vehicle = None
              for vehicle in veh_baidu_list:
                  if vehicle.get_trip() is not None:
                      continue
                  best_vehicle = vehicle
                  task_release_time = aircraft.get_flight().get_scheduled_arrival_time()+5
                  if dispatch_time > task_release_time:#任务下达时间一定是≥调度时间
                      task_release_time = dispatch_time
                  new_trip = Trip(task_release_time=task_release_time,
                                  destination_x=aircraft.get_flight().get_local_gate_position().get_x(),
                                  destination_y=aircraft.get_flight().get_local_gate_position().get_y())
              if best_vehicle == None:
                  print("没有车辆")
                  break
              best_vehicle.set_trip(new_trip)
              best_vehicle.set_aircraft(aircraft)
              best_vehicle.generate_departure_gate_position_event()
              aircraft.set_status(2)
              aircraft.set_baidu_status(2)

    for aircraft in air_list:
        if aircraft.get_flight().get_category() == 1:
          if (aircraft.get_jiayou_status()==1)&(dispatch_time>=aircraft.get_flight().get_scheduled_departure_time()-70): 
              best_vehicle = None
              for vehicle in veh_jiayou_list:
                  if vehicle.get_trip() is not None:
                      continue
                  best_vehicle = vehicle
                  if aircraft.get_flight().get_category() == 1:#离港
                      task_release_time = aircraft.get_flight().get_scheduled_departure_time()-70
                  else:
                      task_release_time = aircraft.get_flight().get_scheduled_arrival_time() - 20
                  if dispatch_time > task_release_time:#任务下达时间一定是≥调度时间
                      task_release_time = dispatch_time
                  new_trip = Trip(task_release_time=task_release_time,
                                  destination_x=aircraft.get_flight().get_local_gate_position().get_x(),
                                  destination_y=aircraft.get_flight().get_local_gate_position().get_y())
           
              if best_vehicle == None:
                  print("没有车辆")
                  break
              best_vehicle.set_trip(new_trip)
              best_vehicle.set_aircraft(aircraft)
              best_vehicle.generate_departure_gate_position_event()
              aircraft.set_status(2)
              aircraft.set_jiayou_status(2)
            
    for aircraft in air_list:    
        if aircraft.get_flight().get_category() == 1:
          if (aircraft.get_xingli_status()==1)&(dispatch_time>=aircraft.get_flight().get_scheduled_departure_time()-70):
              best_vehicle = None
              for vehicle in veh_xingli_list:
                  if vehicle.get_trip() is not None:
                      continue
                  best_vehicle = vehicle
                  if aircraft.get_flight().get_category() == 1:#离港
                      task_release_time = aircraft.get_flight().get_scheduled_departure_time()-70#这里的时间需要考虑行李车行驶时间+服务时间+牵引车服务时间25+20
                  else:
                      task_release_time = aircraft.get_flight().get_scheduled_arrival_time() - 20
                  if dispatch_time > task_release_time:#任务下达时间一定是≥调度时间
                      task_release_time = dispatch_time
                  new_trip = Trip(task_release_time=task_release_time,
                                  destination_x=aircraft.get_flight().get_local_gate_position().get_x(),
                                  destination_y=aircraft.get_flight().get_local_gate_position().get_y())
             
              if best_vehicle == None:
                  print("没有车辆")
                  break
              best_vehicle.set_trip(new_trip)
              best_vehicle.set_aircraft(aircraft)
              best_vehicle.generate_departure_gate_position_event()
              aircraft.set_status(2)
              aircraft.set_xingli_status(2)
       
        else:
          if (aircraft.get_xingli_status()==1)&(dispatch_time>=aircraft.get_flight().get_scheduled_arrival_time()+5):
              best_vehicle = None
              for vehicle in veh_xingli_list:
                  if vehicle.get_trip() is not None:
                      continue
                  best_vehicle = vehicle
                  task_release_time = aircraft.get_flight().get_scheduled_arrival_time()+5
                  if dispatch_time > task_release_time:#任务下达时间一定是≥调度时间
                      task_release_time = dispatch_time
                  new_trip = Trip(task_release_time=task_release_time,
                                  destination_x=aircraft.get_flight().get_local_gate_position().get_x(),
                                  destination_y=aircraft.get_flight().get_local_gate_position().get_y())
              if best_vehicle == None:
                  print("没有车辆")
                  break
              best_vehicle.set_trip(new_trip)
              best_vehicle.set_aircraft(aircraft)
              best_vehicle.generate_departure_gate_position_event()
              aircraft.set_status(2)
              aircraft.set_xingli_status(2)
              
              
    for aircraft in air_list:
        if aircraft.get_flight().get_category() == 0:
          if (aircraft.get_laji_status()==1)&(dispatch_time>=aircraft.get_flight().get_scheduled_arrival_time()+5):
              best_vehicle = None
              for vehicle in veh_laji_list:
                  if vehicle.get_trip() is not None:
                      continue
                  best_vehicle = vehicle
                  task_release_time = aircraft.get_flight().get_scheduled_arrival_time()+5
                  if dispatch_time > task_release_time:#任务下达时间一定是≥调度时间
                      task_release_time = dispatch_time
                  new_trip = Trip(task_release_time=task_release_time,
                                  destination_x=aircraft.get_flight().get_local_gate_position().get_x(),
                                  destination_y=aircraft.get_flight().get_local_gate_position().get_y())
              if best_vehicle == None:
                  print("没有车辆")
                  break
              best_vehicle.set_trip(new_trip)
              best_vehicle.set_aircraft(aircraft)
              best_vehicle.generate_departure_gate_position_event()
              aircraft.set_status(2)
              aircraft.set_laji_status(2)
              
              
    for aircraft in air_list:
        if aircraft.get_flight().get_category() == 0:
          if (aircraft.get_wushui_status()==1)&(dispatch_time>=aircraft.get_flight().get_scheduled_arrival_time()+5):
              best_vehicle = None
              for vehicle in veh_wushui_list:
                  if vehicle.get_trip() is not None:
                      continue
                  best_vehicle = vehicle
                  task_release_time = aircraft.get_flight().get_scheduled_arrival_time()+5
                  if dispatch_time > task_release_time:#任务下达时间一定是≥调度时间
                      task_release_time = dispatch_time
                  new_trip = Trip(task_release_time=task_release_time,
                                  destination_x=aircraft.get_flight().get_local_gate_position().get_x(),
                                  destination_y=aircraft.get_flight().get_local_gate_position().get_y())
              if best_vehicle == None:
                  print("没有车辆")
                  break
              best_vehicle.set_trip(new_trip)
              best_vehicle.set_aircraft(aircraft)
              best_vehicle.generate_departure_gate_position_event()
              aircraft.set_status(2)
              aircraft.set_wushui_status(2)
              
              
    for aircraft in air_list:
        if aircraft.get_flight().get_category() == 1:
          if (aircraft.get_qingshui_status()==1)&(dispatch_time>=aircraft.get_flight().get_scheduled_departure_time()-50):
              best_vehicle = None
              for vehicle in veh_qingshui_list:
                  if vehicle.get_trip() is not None:
                      continue
                  best_vehicle = vehicle
                  if aircraft.get_flight().get_category() == 1:#离港
                      task_release_time = aircraft.get_flight().get_scheduled_departure_time()-50#这里的时间需要考虑行李车行驶时间+服务时间+牵引车服务时间25+20
                  else:
                      task_release_time = aircraft.get_flight().get_scheduled_arrival_time() - 20
                  if dispatch_time > task_release_time:#任务下达时间一定是≥调度时间
                      task_release_time = dispatch_time
                  new_trip = Trip(task_release_time=task_release_time,
                                  destination_x=aircraft.get_flight().get_local_gate_position().get_x(),
                                  destination_y=aircraft.get_flight().get_local_gate_position().get_y())
             
              if best_vehicle == None:
                  print("没有车辆")
                  break
              best_vehicle.set_trip(new_trip)
              best_vehicle.set_aircraft(aircraft)
              best_vehicle.generate_departure_gate_position_event()
              aircraft.set_status(2)
              aircraft.set_qingshui_status(2)

    for aircraft in air_list:
        if aircraft.get_flight().get_category() == 1:
          if (aircraft.get_shipin_status()==1)&(dispatch_time>=aircraft.get_flight().get_scheduled_departure_time()-50):
              best_vehicle = None
              for vehicle in veh_shipin_list:
                  if vehicle.get_trip() is not None:
                      continue
                  best_vehicle = vehicle
                  if aircraft.get_flight().get_category() == 1:#离港
                      task_release_time = aircraft.get_flight().get_scheduled_departure_time()-50#这里的时间需要考虑行李车行驶时间+服务时间+牵引车服务时间25+20
                  else:
                      task_release_time = aircraft.get_flight().get_scheduled_arrival_time() - 20
                  if dispatch_time > task_release_time:#任务下达时间一定是≥调度时间
                      task_release_time = dispatch_time
                  new_trip = Trip(task_release_time=task_release_time,
                                  destination_x=aircraft.get_flight().get_local_gate_position().get_x(),
                                  destination_y=aircraft.get_flight().get_local_gate_position().get_y())
           
              if best_vehicle == None:
                  print("没有车辆")
                  break
              best_vehicle.set_trip(new_trip)
              best_vehicle.set_aircraft(aircraft)
              best_vehicle.generate_departure_gate_position_event()
              aircraft.set_status(2)
              aircraft.set_shipin_status(2)

    for aircraft in air_list:
        if aircraft.get_flight().get_category() == 1: #离港
          if (aircraft.get_qianyin_status()==1)&(dispatch_time>=aircraft.get_flight().get_scheduled_departure_time()-35):
              best_vehicle = None
              for vehicle in veh_list:
                  if vehicle.get_trip() is not None:
                      continue
                  best_vehicle = vehicle
                  task_release_time = aircraft.get_flight().get_scheduled_departure_time()-35#这里的时间需要考虑牵引车行驶时间+服务时间
                      
                  if dispatch_time > task_release_time:#任务下达时间一定是≥调度时间
                      task_release_time = dispatch_time
                  new_trip = Trip(task_release_time=task_release_time,
                                  destination_x=aircraft.get_flight().get_local_gate_position().get_x(),
                                  destination_y=aircraft.get_flight().get_local_gate_position().get_y())
           
              if best_vehicle == None:
                  print("没有车辆")
                  break
              best_vehicle.set_trip(new_trip)
              best_vehicle.set_aircraft(aircraft)
              best_vehicle.generate_departure_gate_position_event()
              aircraft.set_status(2)
              aircraft.set_qianyin_status(2)
        
        else:
          if (aircraft.get_qianyin_status()==1)&(dispatch_time>=aircraft.get_flight().get_scheduled_arrival_time()-15):
              best_vehicle = None
              for vehicle in veh_list:
                  if vehicle.get_trip() is not None:
                      continue
                  best_vehicle = vehicle
                  task_release_time = aircraft.get_flight().get_scheduled_arrival_time()-15
                      
                  if dispatch_time > task_release_time:#任务下达时间一定是≥调度时间
                      task_release_time = dispatch_time
                  new_trip = Trip(task_release_time=task_release_time,
                                  destination_x=aircraft.get_flight().get_local_gate_position().get_x(),
                                  destination_y=aircraft.get_flight().get_local_gate_position().get_y())
           
              if best_vehicle == None:
                  print("没有车辆")
                  break
              best_vehicle.set_trip(new_trip)
              best_vehicle.set_aircraft(aircraft)
              best_vehicle.generate_departure_gate_position_event()
              aircraft.set_status(2)
              aircraft.set_qianyin_status(2)
        
        
        
"""
def distance_match(dispatch_time, vehicle_list: list, aircraft_list: list):#调度时间
    best_vehicle = None
    veh_list = vehicle_list.copy()
    air_list = aircraft_list.copy()#所有当前已知需要服务航班要按时间排序(40min内)
    print('veh_list',[veh.get_name() for veh in veh_list])
    print('air_list',[air.get_aircraft_id() for air in air_list])
    
    for aircraft in air_list:
        min_distance = 1000000
        if aircraft.get_flight().get_category() == 1:#离港
            task_release_time = aircraft.get_flight().get_scheduled_departure_time() - 4*10#任务下达时间=航班计划时间之前10分钟(但是存在调度时间已经在此时间之后的情况)
        else:
            task_release_time = aircraft.get_flight().get_scheduled_arrival_time() - 20
        if dispatch_time > task_release_time:#任务下达时间一定是≥调度时间
            task_release_time = dispatch_time

        new_trip = Trip(task_release_time=task_release_time,
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
            break#一旦匹配到空闲车辆就不再寻找车辆（从车辆中循环跳出），开始下一个aircraft循环
"""
