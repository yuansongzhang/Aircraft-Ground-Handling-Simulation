#from ground_handling import GroundHandling

class EventDispatcher:
    def __init__(self, aircraft_list, vehicle_list, vehicle_xingli_list, vehicle_jiayou_list, vehicle_baidu_list, vehicle_shipin_list, vehicle_qingshui_list, vehicle_laji_list, vehicle_wushui_list, ground_handling):#?ground_handling没用？
        self.__aircraft_list = aircraft_list
        self.__vehicle_list = vehicle_list
        self.__vehicle_xingli_list = vehicle_xingli_list
        self.__vehicle_jiayou_list = vehicle_jiayou_list
        self.__vehicle_baidu_list = vehicle_baidu_list
        self.__vehicle_shipin_list = vehicle_shipin_list
        self.__vehicle_qingshui_list = vehicle_qingshui_list
        self.__vehicle_laji_list = vehicle_laji_list
        self.__vehicle_wushui_list = vehicle_wushui_list
        self.__ground_handling = ground_handling

    def is_finished(self):
        for aircraft in self.__aircraft_list:#8
            if aircraft.get_current_event() is not None:
                return False#9
        if self.__vehicle_list is None:
            return True
        if self.__vehicle_xingli_list is None:
            return True
        if self.__vehicle_jiayou_list is None:
            return True
        if self.__vehicle_baidu_list is None:
            return True
        if self.__vehicle_shipin_list is None:
            return True
        if self.__vehicle_qingshui_list is None:
            return True
        if self.__vehicle_laji_list is None:
            return True
        if self.__vehicle_wushui_list is None:
            return True
        else:
            for veh in self.__vehicle_list:
                if veh.get_servicestatus() == 1:#在服务中
                    return False
            for veh in self.__vehicle_xingli_list:
                if veh.get_servicestatus() == 1:#在服务中
                    return False
            for veh in self.__vehicle_jiayou_list:
                if veh.get_servicestatus() == 1:#在服务中
                    return False
            for veh in self.__vehicle_baidu_list:
                if veh.get_servicestatus() == 1:#在服务中
                    return False
            for veh in self.__vehicle_shipin_list:
                if veh.get_servicestatus() == 1:#在服务中
                    return False
            for veh in self.__vehicle_qingshui_list:
                if veh.get_servicestatus() == 1:#在服务中
                    return False
            for veh in self.__vehicle_laji_list:
                if veh.get_servicestatus() == 1:#在服务中
                    return False
            for veh in self.__vehicle_wushui_list:
                if veh.get_servicestatus() == 1:#在服务中
                    return False
        return True




'''
class EventDispatcher:
    def __init__(self, aircraft_list):
        self.__aircraft_list = aircraft_list
        self.aircraft=aircraft_list[1]
     
    def is_finished(self):
        for aircraft in self.__aircraft_list:
            if aircraft.get_current_event() is not None:
                return False
        return True
'''  
    
    
    
    
"""
def execute(self):
    current_ground_handling=GroundHandling(0)
    current_ground_handling.aircraft=self.aircraft
    self.current_ground_handling=current_ground_handling
    self.current_ground_handling.generate_dispatch_event()
    self.current_ground_handling.dispatch_event_update()
    self.current_ground_handling.best_vehicle.generate_arrival__gate_position_event()
    self.current_ground_handling.best_vehicle.arrival__gate_position_event_update()
    self.current_ground_handling.aircraft.generate_arrival_gate_position_event()
    self.current_ground_handling.aircraft.arrival_gate_position_event_update()
    self.current_ground_handling.best_vehicle.generate_service_event()
    self.current_ground_handling.best_vehicle.service_event_update()
    self.current_ground_handling.best_vehicle.generate_departure_gate_position_event()
    self.current_ground_handling.best_vehicle.departure__gate_position_event_update()
    self.current_ground_handling.aircraft.generate_departure_gate_position_event()
    self.current_ground_handling.aircraft.departure_gate_position_event_update()
   # for i in range(0,100):
   #   if vehicle_list[i].name==self.current_ground_handling.best_vehicle.name:
   #     vehivle_list[i]=self.current_ground_handling.vehicle.name
   #     break
   # for i in range(0,1000)
   #   aircraft_list[i]=aircraft_list[i+1]
  """