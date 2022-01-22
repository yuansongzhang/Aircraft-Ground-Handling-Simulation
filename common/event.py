# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


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
        # todo: interaction with vehicles, random travel timestamp
        self._triggering_timestamp = aircraft.get_flight().get_real_departure_timestamp()
        delay_time = 0
        #delay_timestamp = vehicle.__currentevent.service_finish_timestamp
        self._triggering_timestamp = self._triggering_timestamp + delay_time 
        
        self.__departure_gate_position = aircraft.get_flight().get_local_gate_position()
        self.__departure_timestamp = self._triggering_timestamp

    def execute(self):
        # updates aircraft.
        self.__aircraft.get_flight().set_real_departure_timestamp(self.__departure_timestamp)
        self.__aircraft.set_status(0)
        self.__aircraft.aircraft_departure_gate_position_event_update()
        # generates next event.
        #self.__aircraft.generate_arrival_gate_position_event() 


class AircraftArrivalGatePositionEvent(Event):
    "飞行器到达事件"
    
    def __init__(self, aircraft):
        super().__init__()
        self.__aircraft = aircraft
        self.__arrival_gate_position = None
        self.__arrival_timestamp = None
        self.__last_arrival_timestamp = None
        self.update()

    def update(self):
        aircraft = self.__aircraft
        # todo: interaction with vehicles
        self._triggering_timestamp = aircraft.get_flight().get_real_arrival_timestamp()
        self.__arrival_gate_position = aircraft.get_flight().get_local_gate_position()
        self.__arrival_timestamp = self._triggering_timestamp

    def execute(self):
        # updates aircraft.

        self.__aircraft.set_status(0)
        self.__aircraft.aircraft_arrival_gate_position_event_update()
        # ends with arrival gate position and does not generate any event.


class VehicleDepartureGatePositionEvent(Event):
    def __init__(self, vehicle):
        super().__init__()
        # self.__ssession_start_timestamp = None #新添，冗余应该没啥用
        self.__vehicle = vehicle
        self.__departure_x = None #改变
        self.__departure_y = None
        self.__departure_timestamp = None
        self.update()

    def update(self):
        vehicle = self.__vehicle
        # todo: interaction with aircraft
        # self.__ssession_start_timestamp = vehicle.get_trip().get_task_release_timestamp()
        self._triggering_timestamp = vehicle.get_trip().get_task_release_timestamp()
        self.__departure_x = vehicle.get_x()
        self.__departure_y = vehicle.get_y()
        self.__departure_timestamp = self._triggering_timestamp

    def execute(self):
        # updates vehicle.
        self.__vehicle.get_trip().set_departure_timestamp(self.__departure_timestamp)
        self.__vehicle.departure_gate_position_event_update()
        # generates next event.
        self.__vehicle.generate_arrival_gate_position_event()


class VehicleArrivalGatePositionEvent(Event):
    def __init__(self, vehicle):
        super().__init__()
        self.__vehicle = vehicle
        #self.__arrival_gate_position = None
        self.__arrival_x = None
        self.__arrival_y = None
        self.__arrival_timestamp = None
        self.update()

    def update(self):
        vehicle = self.__vehicle
        # todo: random trip timestamp, interaction with aircraft
        self._triggering_timestamp = vehicle.get_trip().get_departure_timestamp() + 9 #9是车辆行程时间
        self.__arrival_x = vehicle.get_trip().get_destination_x() #destination在匹配中会改变,匹配中同时要改变xy
        self.__arrival_y = vehicle.get_trip().get_destination_y()
        #改！！
        self.__arrival_timestamp = self._triggering_timestamp

    def execute(self):
        # updates vehicle.
        self.__vehicle.get_trip().set_arrival_timestamp(self.__arrival_timestamp)
        self.__vehicle.arrival_gate_position_event_update()
        # generates next event.
        self.__vehicle.generate_service_event()


class VehicleServiceEvent(Event):
    def __init__(self, vehicle):
        super().__init__()
        self.__vehicle = vehicle
        self.__service_start_timestamp = None
        self.__service_finish_timestamp = None
        self.update()

    def update(self):
        vehicle = self.__vehicle
        # todo: random service timestamp
        self.__service_time = 10
        
        if vehicle.get_aircraft().get_flight().get_category()==0: #到港
            if self.__vehicle.get_aircraft().get_flight().get_real_arrival_timestamp()-self.__vehicle.get_trip().get_arrival_timestamp() >=120:#飞机实际到达时间-车辆到达时间>120min
                self._triggering_timestamp = vehicle.get_aircraft().get_flight().get_scheduled_arrival_timestamp()
            elif (vehicle.get_aircraft().get_flight().get_real_arrival_timestamp()>=vehicle.get_trip().get_arrival_timestamp())&( self.__vehicle.get_aircraft().get_flight().get_real_arrival_timestamp()-self.__vehicle.get_trip().get_arrival_timestamp() <120):
                self._triggering_timestamp = vehicle.get_aircraft().get_flight().get_real_arrival_timestamp()#120时间有点长
            elif vehicle.get_aircraft().get_flight().get_real_arrival_timestamp()<vehicle.get_trip().get_arrival_timestamp():#飞机比车辆早到  
                self._triggering_timestamp = vehicle.get_trip().get_arrival_timestamp()
        
        elif vehicle.get_aircraft().get_flight().get_category()==1: #离港
            if vehicle.get_aircraft().get_flight().get_real_departure_time()-vehicle.get_trip().get_arrival_time()>=140:#航班真正离港时间-车辆到达时间≥140
                self._triggering_timestamp = vehicle.get_aircraft().get_flight().get_scheduled_departure_timestamp()-20
            elif (vehicle.get_aircraft().get_flight().get_real_departure_timestamp()-140<vehicle.get_trip().get_arrival_timestamp())&(vehicle.get_aircraft().get_flight().get_real_departure_timestamp()-20>=vehicle.get_trip().get_arrival_timestamp()):#20≤航班真正离港时间-车辆到达时间≤140
                self._triggering_timestamp = vehicle.get_aircraft().get_flight().get_real_departure_timestamp()-20
            elif vehicle.get_aircraft().get_flight().get_real_departure_timestamp()-20<vehicle.get_trip().get_arrival_timestamp():#航班真正离港时间-车辆到达时间≤20
                self._triggering_timestamp = vehicle.get_trip().get_arrival_timestamp()
        
        self.__service_start_timestamp = self._triggering_timestamp


    def execute(self):
        # updates vehicle.
      if self.__vehicle.get_aircraft().get_flight().get_category()==0: #到港
        if self.__vehicle.get_aircraft().get_flight().get_real_arrival_timestamp()-self.__vehicle.get_trip().get_arrival_timestamp() >=120:
          self.__vehicle.get_trip().set_service_time(0)
          self.__service_finish_timestamp=max(self.__vehicle.get_trip().get_arrival_timestamp(),self.__vehicle.get_aircraft().get_flight().get_scheduled_arrival_timestamp())        
        if self.__vehicle.get_aircraft().get_flight().get_real_arrival_timestamp()-self.__vehicle.get_trip().get_arrival_timestamp() <120: 
          self.__vehicle.get_trip().set_service_time(self.__service_time)
          self.__service_finish_timestamp=self.__service_start_timestamp +self.__service_time
      
      elif self.__vehicle.get_aircraft().get_flight().get_category()==1: #离港
        if self.__vehicle.get_aircraft().get_flight().get_real_departure_timestamp()-self.__vehicle.get_trip().get_arrival_timestamp() >=120:
          self.__vehicle.get_trip().set_service_time(0)
          self.__service_finish_timestamp=self.__vehicle.get_aircraft().get_flight().get_scheduled_departure_timestamp()-20
        if self.__vehicle.get_aircraft().get_flight().get_real_departure_timestamp()-self.__vehicle.get_trip().get_arrival_timestamp() <120: 
          self.__vehicle.get_trip().set_service_time(self.__service_time)
          self.__service_finish_timestamp=self.__service_start_timestamp +self.__service_time
      self.__vehicle.get_trip().set_service_finish_timestamp(self.__service_finish_timestamp)
      self.__vehicle.service_event_update()
      if self.__vehicle.get_trip().get_service_time()==0:
          self.__vehicle.generate_status_turn_to_0_event()
      else:
          self.__vehicle.generate_return_and_prepare_start_event()

class VehicleReturnAndPrepareStartEvent(Event):
    def __init__(self, vehicle):
        super().__init__()
        self.__vehicle = vehicle
        self.__arrival_x = None #这里的xy指准备的同一地点1，1
        self.__arrival_y = None
        self.__prepare_start_timestamp = None
        self.update()

    def update(self):
        vehicle = self.__vehicle
        self._triggering_timestamp = vehicle.get_trip().get_service_finish_timestamp() #10是车辆返回时间
        self.__arrival_x = 1 #初始test时设置坐标为1，1
        self.__arrival_y = 1
        self.__prepare_start_timestamp = self._triggering_timestamp+10
        
    def execute(self):
        # updates vehicle.
        self.__vehicle.get_trip().set_prepare_start_timestamp(self.__prepare_start_timestamp)
        self.__vehicle.return_and_prepare_start_event_update()
        # generates next event.
        self.__vehicle.generate_prepare_finish_event()
        
        
class VehiclePrepareFinishEvent(Event): 
    def __init__(self, vehicle):
        super().__init__()
        self.__vehicle = vehicle
        self.__prepare_timestamp = None #prepare_timestamp包括车辆回到准备地点+准备的时间
        self.__prepare_finish_timestamp = None
        self.update()

    def update(self):
        vehicle = self.__vehicle
        if vehicle.get_trip().get_service_time()==0:
          self.__prepare_time = 0
        else:
          self.__prepare_time = 10
        self._triggering_timestamp = vehicle.get_trip().get_prepare_start_timestamp()
        self.__prepare_finish_timestamp = self._triggering_timestamp + self.__prepare_time #准备完成时间
        
    def execute(self):
        # updates vehicle.
        self.__vehicle.get_trip().set_prepare_time(self.__prepare_time)
        self.__vehicle.get_trip().set_prepare_finish_timestamp(self.__prepare_finish_timestamp)
        self.__vehicle.prepare_finish_event_update()
        self.__vehicle.generate_status_turn_to_0_event()
        

class VehicleStatusTurnTo0Event(Event):
    def __init__(self, vehicle):
        super().__init__()
        self.__vehicle = vehicle
        self.__status_turn_to_0_timestamp = None
        self.update()

    def update(self):
        vehicle = self.__vehicle
        if vehicle.get_trip().get_service_time()==0:
            self._triggering_timestamp=vehicle.get_trip().get_service_finish_timestamp()
        else:
            self._triggering_timestamp = vehicle.get_trip().get_prepare_finish_timestamp()
        self.__status_turn_to_0_timestamp = self._triggering_timestamp
        
    def execute(self):
        # updates vehicle.
        self.__vehicle.get_trip().set_status_turn_to_0_timestamp(self.__status_turn_to_0_timestamp)
        self.__vehicle.status_turn_to_0_event_update()
        # finishes the current trip and does not generate any event.

class GroundHandlingDispatchEvent(Event):
    def __init__(self, ground_handling):
        super().__init__()
        self.__ground_handling = ground_handling
        self.__dispatch_timestamp = None
        self.update()

    def update(self):
        ground_handling = self.__ground_handling
        self._triggering_timestamp = ground_handling.get_last_dispatch_timestamp() + ground_handling.get_dispatch_interval()
        self.__dispatch_timestamp = self._triggering_timestamp #本次匹配时间是上次匹配时间加上匹配间隔

    def execute(self):
        # updates ground handling.
        self.__ground_handling.set_dispatch_timestamp(self.__dispatch_timestamp)
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
        self._triggering_timestamp = ground_handling.get_dispatch_timestamp()

    def execute(self, *args, **kwargs):
        # updates ground handling.
        self.__ground_handling.waiting_event_update()
        # generates next event.
        self.__ground_handling.generate_dispatch_event()
        
        
        
        
        