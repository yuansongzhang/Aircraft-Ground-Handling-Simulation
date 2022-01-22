# -*- coding: utf-8 -*-
from .gate_position import GatePosition


class Flight:  # 类似原文件中trip
    def __init__(self,
                 category,
                 id,
                 scheduled_departure_timestamp,
                 scheduled_arrival_timestamp,
                 real_departure_timestamp,
                 real_arrival_timestamp,
                 local_gate_position: GatePosition,
                 other_gate_position: GatePosition,
                 # layover_time
                 ):
        self.__id=id #航班号或其它代码
        self.__category = category  # 到港离港 0到港 1离港
        self.__scheduled_departure_timestamp = scheduled_departure_timestamp  # 预计离开时间
        self.__scheduled_arrival_timestamp = scheduled_arrival_timestamp  # 预计到达时间
        self.__local_gate_position = local_gate_position  # 浦东机场停机位
        self.__other_gate_position = other_gate_position,  # 虚拟机场停机位
        self.__real_departure_timestamp =real_departure_timestamp    # 实际离开时间，前期用不到
        self.__real_arrival_timestamp = real_arrival_timestamp  # 实际到达时间，前期用不到
        # self.__layover_time = layover_time  # 飞机可以停留时间

    def set_real_departure_timestamp(self, real_departure_timestamp):
        self.__real_departure_timestamp = real_departure_timestamp

    def set_real_arrival_timestamp(self, real_arrival_timestamp):
        self.__real_arrival_timestamp = real_arrival_timestamp

    def get_category(self):  # type到港离港
        return self.__category
    
    def set_scheduled_arrival_timestamp(self):
        self.__scheduled_arrival_timestamp=self.__real_arrival_timestamp#把真正时间赋给计划时间
        
    def set_scheduled_departure_timestamp(self):
        self.__scheduled_departure_timestamp=self.__real_departure_timestamp
    """
    def getLeisureTime(self):
        return self.__layover_time

    def get_layover_time(self):
        return self.__layover_time
    """
    def get_scheduled_departure_timestamp(self):
        return self.__scheduled_departure_timestamp

    def get_scheduled_arrival_timestamp(self):
        return self.__scheduled_arrival_timestamp

    def get_local_gate_position(self):
        return self.__local_gate_position

    def get_other_gate_position(self):
        return self.__other_gate_position

    def get_real_departure_timestamp(self):
        return self.__real_departure_timestamp

    def get_real_arrival_timestamp(self):
        return self.__real_arrival_timestamp
    def get_id(self):
        return self.__id