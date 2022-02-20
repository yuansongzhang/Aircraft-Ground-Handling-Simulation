# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import numpy as np


class Event:
    __meta_class__ = ABCMeta

    def __init__(self):
        self._triggering_timestamp = None

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    def get_triggering_timestamp(self):
        return self._triggering_timestamp


class AircraftDepartureGatePositionEvent(Event):
    "飞行器离开事件"
    
    def __init__(self, aircraft):
        super().__init__()
        self.__aircraft = aircraft
        self.__departure_gate_position = None
        self.__departure_timestamp = None
        self.update()

    def update(self):
        aircraft = self.__aircraft
        # todo: interaction with vehicles, random travel time
        self._triggering_timestamp = aircraft.get_final_departure_timestamp()
        
        #self.__departure_gate_position = aircraft.get_flight().get_local_gate_position()
        self.__departure_timestamp = self._triggering_timestamp

    def execute(self):
        # updates aircraft.
        #self.__aircraft.get_flight().set_real_departure_time(self.__departure_timestamp)
        #self.__aircraft.set_status(0)
        self.__aircraft.aircraft_departure_gate_position_event_update()
        # generates next event.
        #self.__aircraft.generate_arrival_gate_position_event() 


class AircraftArrivalGatePositionEvent(Event):
    "飞行器到达事件"
    def __init__(self, aircraft):
        super().__init__()
        self.__aircraft = aircraft
        #self.__arrival_gate_position = None
        self.__arrival_timestamp = None
        #self.__last_arrival_timestamp = None
        self.update()

    def update(self):
        aircraft = self.__aircraft
        # todo: interaction with vehicles
        self._triggering_timestamp = aircraft.get_arrive_qianyin_start_timestamp() #牵引车服务一开始，飞机到港事件就完成了
        #self.__arrival_gate_position = aircraft.get_flight().get_local_gate_position()
        self.__arrival_timestamp = self._triggering_timestamp

    def execute(self):
        # updates aircraft.
        self.__aircraft.set_status(2) #飞机已经到港但是系列到港服务还未完成
        self.__aircraft.aircraft_arrival_gate_position_event_update()
        self.__aircraft.generate_arrival_service_finish_event() 


class AircraftArrivalServiceFinishEvent(Event):
    def __init__(self, aircraft):
        super().__init__()
        self.__aircraft = aircraft
        self.__arrival_service_finish_timestamp = None
        self.update()

    def update(self):
        aircraft = self.__aircraft
        self._triggering_timestamp = max(aircraft.get_arrive_baidu_finish_timestamp(),aircraft.get_arrive_xingli_finish_timestamp(),aircraft.get_arrive_wushui_finish_timestamp(),aircraft.get_arrive_laji_finish_timestamp())
        self.__arrival_service_finish_timestamp = self._triggering_timestamp

    def execute(self):
        self.__aircraft.set_status(0) #飞机到港服务已全部完成
        self.__aircraft.arrival_service_finish_event_update()
        # ends with arrival gate position and does not generate any event.


class VehicleDepartureGatePositionEvent(Event):
    def __init__(self, vehicle):
        super().__init__()
        self.__vehicle = vehicle
        self.__departure_x = None #改变
        self.__departure_y = None
        self.__departure_timestamp = None
        self.update()

    def update(self):
        vehicle = self.__vehicle
        self._triggering_timestamp = vehicle.get_trip().get_task_release_time()
        self.__departure_x = vehicle.get_x()
        self.__departure_y = vehicle.get_y()
        self.__departure_timestamp = self._triggering_timestamp

    def execute(self):
        self.__vehicle.get_trip().set_departure_time(self.__departure_timestamp)
        self.__vehicle.departure_gate_position_event_update()
        self.__vehicle.generate_arrival_gate_position_event()


class VehicleArrivalGatePositionEvent(Event):
    def __init__(self, vehicle):
        super().__init__()
        self.__vehicle = vehicle
        self.__arrival_x = None
        self.__arrival_y = None
        self.__arrival_timestamp = None
        self.__length = None
        self.update()

    def update(self):
        vehicle = self.__vehicle
        self.__arrival_x = vehicle.get_trip().get_destination_x() #destination在匹配中会改变,匹配中同时要改变xy
        self.__arrival_y = vehicle.get_trip().get_destination_y()
        #speed = vehicle.get__v()
        #self.__length = np.sqrt(np.square(vehicle.get_x()-self.__arrival_x)+np.square(vehicle.get_y()-self.__arrival_y))
        self._triggering_timestamp = vehicle.get_trip().get_departure_time() + 9#self.__length/speed #10是车辆行程时间
        self.__arrival_timestamp = self._triggering_timestamp

    def execute(self):
        self.__vehicle.get_trip().set_arrival_time(self.__arrival_timestamp)
        self.__vehicle.arrival_gate_position_event_update()
        self.__vehicle.generate_service_event()
    


class VehicleServiceEvent(Event): #其实是牵引车service开始
    def __init__(self, vehicle):
        super().__init__()
        self.__vehicle = vehicle
        self.__service_time = None
        self.__service_start_time = None
        self.__service_finish_time = None
        self.update()

    def update(self):
        vehicle = self.__vehicle
        # todo: random service time
        self.__service_time = np.random.randint(15,25)
        #self.__service_time = 10
        if vehicle.get_aircraft().get_flight().get_category()==0: #到港
            if self.__vehicle.get_aircraft().get_flight().get_real_arrival_time()-self.__vehicle.get_trip().get_arrival_time() >=50:
                self._triggering_timestamp = vehicle.get_trip().get_arrival_time()
            if (vehicle.get_aircraft().get_flight().get_real_arrival_time()>=vehicle.get_trip().get_arrival_time())&(self.__vehicle.get_aircraft().get_flight().get_real_arrival_time()-self.__vehicle.get_trip().get_arrival_time()<50):
                self._triggering_timestamp = vehicle.get_aircraft().get_flight().get_real_arrival_time()
            elif vehicle.get_aircraft().get_flight().get_real_arrival_time()<vehicle.get_trip().get_arrival_time():  
                self._triggering_timestamp = vehicle.get_trip().get_arrival_time()
        elif vehicle.get_aircraft().get_flight().get_category()==1: #离港
            if vehicle.get_aircraft().get_flight().get_real_departure_time()-50-self.__service_time-5>=vehicle.get_trip().get_arrival_time():#50为设置的判断延误阈值时间，-10为服务时间,-5为预留时间
                self._triggering_timestamp = vehicle.get_trip().get_arrival_time()
            elif vehicle.get_aircraft().get_flight().get_real_departure_time()-50-self.__service_time-5<vehicle.get_trip().get_arrival_time():
                self._triggering_timestamp = max(vehicle.get_aircraft().get_departure_shipin_finish_timestamp(),vehicle.get_aircraft().get_departure_qingshui_finish_timestamp(),vehicle.get_aircraft().get_departure_xingli_finish_timestamp(), vehicle.get_aircraft().get_departure_baidu_finish_timestamp(),vehicle.get_aircraft().get_flight().get_real_departure_time()-self.__service_time-5, vehicle.get_trip().get_arrival_time())
        self.__service_start_time = self._triggering_timestamp
        self.__vehicle.get_trip().set_service_start_time(self.__service_start_time)


    def execute(self):
        # updates vehicle.
      if self.__vehicle.get_aircraft().get_flight().get_category()==0: #到港
        if self.__vehicle.get_aircraft().get_flight().get_real_arrival_time()-self.__vehicle.get_trip().get_arrival_time() >=50:
          self.__vehicle.get_trip().set_service_time(0)
          self.__service_finish_time=self.__vehicle.get_trip().get_arrival_time()
        if self.__vehicle.get_aircraft().get_flight().get_real_arrival_time()-self.__vehicle.get_trip().get_arrival_time() <50: 
          self.__vehicle.get_trip().set_service_time(self.__service_time)
          self.__service_finish_time=self._triggering_timestamp +self.__service_time
      elif self.__vehicle.get_aircraft().get_flight().get_category()==1: #离港
        if self.__vehicle.get_aircraft().get_flight().get_real_departure_time()-self.__vehicle.get_trip().get_arrival_time() >=55+self.__service_time: #50+10+5
          self.__vehicle.get_trip().set_service_time(0)
          self.__service_finish_time=self.__vehicle.get_trip().get_arrival_time()
        elif self.__vehicle.get_aircraft().get_flight().get_real_departure_time()-self.__vehicle.get_trip().get_arrival_time() <55+self.__service_time: 
          self.__vehicle.get_trip().set_service_time(self.__service_time)
          self.__service_finish_time=self._triggering_timestamp +self.__service_time
      self.__vehicle.get_trip().set_service_finish_time(self.__service_finish_time)
      self.__vehicle.service_event_update()
      if self.__vehicle.get_trip().get_service_time()==0:
          self.__vehicle.generate_status_turn_to_0_event()
      else:
          self.__vehicle.generate_service_finish_event()


class VehicleOtherServiceEvent(Event): #其实是行李车service开始
    def __init__(self, vehicle):
        super().__init__()
        self.__vehicle = vehicle
        self.__service_time = None
        self.__service_start_time = None
        self.__service_finish_time = None
        self.__allow_time = None
        self.update()

    def update(self):
        vehicle = self.__vehicle
        if vehicle.get_aircraft().get_flight().get_category()==1: #离港
            if vehicle.get_vehicle_type()==2: #行李车
                self.__service_time = np.random.randint(30,40) #20
                self.__allow_time = 20+self.__service_time+10 #20为牵引车服务时间，30-40为行李车服务时间，10为预留的阈值 10 20 10
            elif vehicle.get_vehicle_type()==3: #加油车
                self.__service_time = np.random.randint(20,30) #20
                self.__allow_time = 20+8+self.__service_time+10 #20为牵引车服务时间，8为摆渡车服务时间，20为加油车服务时间，10为预留的阈值   10 20 20 10
            elif vehicle.get_vehicle_type()==5: #食品车
                self.__service_time = np.random.randint(10,20) #15
                self.__allow_time = 20+self.__service_time+10 #20为牵引车服务时间，15为食品车服务时间，10为预留的阈值  10 15 10
            elif vehicle.get_vehicle_type()==6: #清水车
                self.__service_time = np.random.randint(14,16) #15
                self.__allow_time = 20+self.__service_time+10 #20为牵引车服务时间，15为食品车服务时间，10为预留的阈值  10 15 10
        elif vehicle.get_aircraft().get_flight().get_category()==0: #进港
            if vehicle.get_vehicle_type()==2: #行李车
                self.__service_time = np.random.randint(20,30) #20
                self.__trig_time = vehicle.get_aircraft().get_arrive_qianyin_finish_add_timestamp()
            elif vehicle.get_vehicle_type()==7: #垃圾车
                self.__service_time = np.random.randint(14,16) 
                self.__trig_time = vehicle.get_aircraft().get_arrive_qianyin_finish_add_timestamp()
            elif vehicle.get_vehicle_type()==8: #污水车
                self.__service_time = np.random.randint(14,16) 
                self.__trig_time = vehicle.get_aircraft().get_arrive_qianyin_finish_add_timestamp()
        if vehicle.get_aircraft().get_flight().get_category()==0: #到港
            if self.__vehicle.get_aircraft().get_flight().get_real_arrival_time()-self.__vehicle.get_trip().get_arrival_time() >=50:
                self._triggering_timestamp = vehicle.get_trip().get_arrival_time()
            else:
                self._triggering_timestamp = max(self.__trig_time, vehicle.get_trip().get_arrival_time())
        elif vehicle.get_aircraft().get_flight().get_category()==1: #离港
            if vehicle.get_aircraft().get_flight().get_real_departure_time()-50-self.__allow_time>=vehicle.get_trip().get_arrival_time():#50为设置的判断延误阈值时间
                self._triggering_timestamp = vehicle.get_trip().get_arrival_time() 
            elif vehicle.get_aircraft().get_flight().get_real_departure_time()-50-self.__allow_time<vehicle.get_trip().get_arrival_time():
                if vehicle.get_vehicle_type()==3 or vehicle.get_vehicle_type()==6: #加油车和清水车没有时间限制
                    self._triggering_timestamp = vehicle.get_trip().get_arrival_time()
                elif vehicle.get_vehicle_type()==2 or vehicle.get_vehicle_type()==5: #行李车和食品车
                    self._triggering_timestamp = max(vehicle.get_aircraft().get_flight().get_real_departure_time()-self.__allow_time, vehicle.get_trip().get_arrival_time())
        self.__service_start_time = self._triggering_timestamp
        self.__vehicle.get_trip().set_service_start_time(self.__service_start_time)

    def execute(self):
        # updates vehicle.
      if self.__vehicle.get_aircraft().get_flight().get_category()==0: #到港
        if self.__vehicle.get_aircraft().get_flight().get_real_arrival_time()-self.__vehicle.get_trip().get_arrival_time() >=50:
          self.__vehicle.get_trip().set_service_time(0)
          self.__service_finish_time=self.__vehicle.get_trip().get_arrival_time()        
        else: 
          self.__vehicle.get_trip().set_service_time(self.__service_time)
          self.__service_finish_time=self._triggering_timestamp +self.__service_time
      elif self.__vehicle.get_aircraft().get_flight().get_category()==1: #离港
        if self.__vehicle.get_aircraft().get_flight().get_real_departure_time()-self.__vehicle.get_trip().get_arrival_time() >=50+self.__allow_time: #50+10+20+10
          self.__vehicle.get_trip().set_service_time(0)
          self.__service_finish_time=self.__vehicle.get_trip().get_arrival_time()
        else: 
          self.__vehicle.get_trip().set_service_time(self.__service_time)
          self.__service_finish_time=self._triggering_timestamp +self.__service_time
      self.__vehicle.get_trip().set_service_finish_time(self.__service_finish_time)
      self.__vehicle.service_event_update()
      if self.__vehicle.get_trip().get_service_time()==0:
          self.__vehicle.generate_status_turn_to_0_event()
      else:
          self.__vehicle.generate_service_finish_event()
          

class VehicleBaiduServiceEvent(Event): #其实是摆渡车service开始，摆渡车和客梯车协同调度
    def __init__(self, vehicle):
        super().__init__()
        self.__vehicle = vehicle
        self.__service_time = None
        self.__service_start_time = None
        self.__service_finish_time = None
        self.update()

    def update(self):
        vehicle = self.__vehicle
        self.__service_time = np.random.randint(5,9) #20
        self.__allow_time = 20+self.__service_time+10 #20为牵引车服务时间，10为预留的阈值  10 20 10
        self.__trig_time = vehicle.get_aircraft().get_arrive_qianyin_finish_add_timestamp()
        if vehicle.get_aircraft().get_flight().get_category()==0: #到港
            if self.__vehicle.get_aircraft().get_flight().get_real_arrival_time()-self.__vehicle.get_trip().get_arrival_time() >=50:
                self._triggering_timestamp = vehicle.get_trip().get_arrival_time()
            else:
                self._triggering_timestamp = max(self.__trig_time, vehicle.get_trip().get_arrival_time())
        elif vehicle.get_aircraft().get_flight().get_category()==1: #离港
            if vehicle.get_aircraft().get_flight().get_real_departure_time()-50-self.__allow_time>=vehicle.get_trip().get_arrival_time():#-50为设置的判断延误阈值时间，-10为牵引车服务时间，-20为摆渡车服务时间，-10为预留的阈值
                self._triggering_timestamp = vehicle.get_trip().get_arrival_time() 
            elif vehicle.get_aircraft().get_flight().get_real_departure_time()-50-self.__allow_time<vehicle.get_trip().get_arrival_time():
                self._triggering_timestamp = max(vehicle.get_aircraft().get_departure_jiayou_finish_timestamp(),vehicle.get_aircraft().get_flight().get_real_departure_time()-self.__allow_time, vehicle.get_trip().get_arrival_time())#-10为牵引车服务时间-20为摆渡车服务时间-10为预留时间
        self.__service_start_time = self._triggering_timestamp
        self.__vehicle.get_trip().set_service_start_time(self.__service_start_time)

    def execute(self):
        # updates vehicle.
      if self.__vehicle.get_aircraft().get_flight().get_category()==0: #到港
        if self.__vehicle.get_aircraft().get_flight().get_real_arrival_time()-self.__vehicle.get_trip().get_arrival_time() >=50:
          self.__vehicle.get_trip().set_service_time(0)
          self.__service_finish_time=self.__vehicle.get_trip().get_arrival_time()
        else: 
          self.__vehicle.get_trip().set_service_time(self.__service_time)
          self.__service_finish_time=self._triggering_timestamp +self.__service_time
      elif self.__vehicle.get_aircraft().get_flight().get_category()==1: #离港
        if self.__vehicle.get_aircraft().get_flight().get_real_departure_time()-self.__vehicle.get_trip().get_arrival_time() >=50+self.__allow_time: #50+10+20+5
          self.__vehicle.get_trip().set_service_time(0)
          self.__service_finish_time=self.__vehicle.get_trip().get_arrival_time()
        if self.__vehicle.get_aircraft().get_flight().get_real_departure_time()-self.__vehicle.get_trip().get_arrival_time() <50+self.__allow_time: 
          self.__vehicle.get_trip().set_service_time(self.__service_time)
          self.__service_finish_time=self._triggering_timestamp +self.__service_time
      self.__vehicle.get_trip().set_service_finish_time(self.__service_finish_time)
      self.__vehicle.service_event_update()
      if self.__vehicle.get_trip().get_service_time()==0:
          self.__vehicle.generate_status_turn_to_0_event()
      else:
          self.__vehicle.generate_service_finish_event()
          
          
class VehicleServiceFinishEvent(Event): #其实是service结束返程开始
    def __init__(self, vehicle):
        super().__init__()
        self.__vehicle = vehicle
        self.__prepare_start_timestamp = None
        self.__length = None
        self.update()

    def update(self):
        vehicle = self.__vehicle
        #speed = vehicle.get__v()
        #self.__length = np.sqrt(np.square(vehicle.get_x())+np.square(vehicle.get_y())) #统一设置车辆准备的坐标为0，0
        self._triggering_timestamp = vehicle.get_trip().get_service_finish_time() 
        self.__prepare_start_timestamp = self._triggering_timestamp + 9#self.__length/speed #车辆返回时间
        
    def execute(self):
        self.__vehicle.get_trip().set_prepare_start_time(self.__prepare_start_timestamp)
        self.__vehicle.service_finish_event_update()
        self.__vehicle.generate_prepare_start_event()
        
        
class VehiclePrepareStartEvent(Event): #其实是返程结束，prepare开始
    def __init__(self, vehicle):
        super().__init__()
        self.__vehicle = vehicle
        #self.__arrival_x = None #这里的xy指准备的同一地点0，0
        #self.__arrival_y = None
        self.__prepare_time = None #prepare_time包括车辆回到准备地点+准备的时间
        self.__prepare_finish_timestamp = None
        self.update()

    def update(self):
        vehicle = self.__vehicle
        #self.__arrival_x = 0 #初始test时设置坐标为0，0
        #self.__arrival_y = 0
        if vehicle.get_vehicle_type()==1: #牵引车
          self.__prepare_time = 3
        elif vehicle.get_vehicle_type()==2: #行李车
          self.__prepare_time = 5
        elif vehicle.get_vehicle_type()==3: #加油车
          self.__prepare_time = 10
        elif vehicle.get_vehicle_type()==4: #摆渡车
          self.__prepare_time = 5
        elif vehicle.get_vehicle_type()==5: #食品车
          self.__prepare_time = 10
        elif vehicle.get_vehicle_type()==6: #清水车
          self.__prepare_time = 10
        elif vehicle.get_vehicle_type()==7: #垃圾车
          self.__prepare_time = 10
        elif vehicle.get_vehicle_type()==8: #污水车
          self.__prepare_time = 10
        self._triggering_timestamp = vehicle.get_trip().get_prepare_start_time()
        self.__prepare_finish_timestamp = self._triggering_timestamp + self.__prepare_time #准备完成时间
        
    def execute(self):
        self.__vehicle.get_trip().set_prepare_time(self.__prepare_time)
        self.__vehicle.get_trip().set_prepare_finish_time(self.__prepare_finish_timestamp)
        self.__vehicle.prepare_start_event_update()
        self.__vehicle.generate_status_turn_to_0_event()
        

class VehicleStatusTurnTo0Event(Event): #prepare结束
    def __init__(self, vehicle):
        super().__init__()
        self.__vehicle = vehicle
        self.__status_turn_to_0_timestamp = None
        self.update()

    def update(self):
        vehicle = self.__vehicle
        if vehicle.get_trip().get_service_time()==0:
            self._triggering_timestamp=vehicle.get_trip().get_service_finish_time()
        else:
            self._triggering_timestamp = vehicle.get_trip().get_prepare_finish_time()
        self.__status_turn_to_0_timestamp = self._triggering_timestamp
        
    def execute(self):
        # updates vehicle.
        self.__vehicle.get_trip().set_status_turn_to_0_time(self.__status_turn_to_0_timestamp)
        self.__vehicle.status_turn_to_0_event_update()
        # finishes the current trip and does not generate any event.

class GroundHandlingDispatchEvent(Event):
    def __init__(self, ground_handling):
        super().__init__()
        self.__ground_handling = ground_handling
        self.__dispatch_time = None
        self.update()

    def update(self):
        ground_handling = self.__ground_handling
        self._triggering_timestamp = ground_handling.get_last_dispatch_time() + ground_handling.get_dispatch_interval()
        self.__dispatch_time = self._triggering_timestamp #本次匹配时间是上次匹配时间加上匹配间隔

    def execute(self):
        # updates ground handling.
        self.__ground_handling.set_dispatch_time(self.__dispatch_time)
        self.__ground_handling.dispatch_event_update()
        # generates next event.
        self.__ground_handling.generate_waiting_event()


class GroundHandlingWaitingEvent(Event):
    def __init__(self, ground_handling):
        super().__init__()
        self.__ground_handling = ground_handling
        self.update()

    def update(self, *args, **kwargs):
        ground_handling = self.__ground_handling
        self._triggering_timestamp = ground_handling.get_dispatch_time()

    def execute(self, *args, **kwargs):
        # updates ground handling.
        self.__ground_handling.waiting_event_update()
        # generates next event.
        self.__ground_handling.generate_dispatch_event()
        
        
        
        
        