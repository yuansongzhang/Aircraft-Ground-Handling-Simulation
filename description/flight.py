# -*- coding: utf-8 -*-
from .gate_position import GatePosition


class Flight:  # 类似原文件中trip
    def __init__(self,
                 category,
                 scheduled_departure_time,
                 scheduled_arrival_time,
                 real_departure_time,
                 real_arrival_time,
                 local_gate_position: GatePosition,
                 other_gate_position: GatePosition,
                 # layover_time
                 ):
        # self.id=id #航班号或其它代码
        self.__category = category  # 到港离港 0到港 1离港
        self.__scheduled_departure_time = scheduled_departure_time  # 预计离开时间
        self.__scheduled_arrival_time = scheduled_arrival_time  # 预计到达时间
        self.__local_gate_position = local_gate_position  # 出发地
        self.__other_gate_position = other_gate_position,  # 目的地
        self.__real_departure_time =real_departure_time    # 实际离开时间，前期用不到
        self.__real_arrival_time = real_arrival_time  # 实际到达时间，前期用不到
        # self.__layover_time = layover_time  # 飞机可以停留时间

    def set_real_departure_time(self, real_departure_time):
        self.__real_departure_time = real_departure_time

    def set_real_arrival_time(self, real_arrival_time):
        self.__real_arrival_time = real_arrival_time

    def get_category(self):  # type到港离港
        return self.__category
    def set_scheduled_arrival_time(self):
        self.__scheduled_arrival_time=self.__real_arrival_time
    def set_scheduled_departure_time(self):
        self.__scheduled_departure_time=self.__real_departure_time
    """
    def getLeisureTime(self):
        return self.__layover_time

    def get_layover_time(self):
        return self.__layover_time
    """
    def get_scheduled_departure_time(self):
        return self.__scheduled_departure_time

    def get_scheduled_arrival_time(self):
        return self.__scheduled_arrival_time

    def get_local_gate_position(self):
        return self.__local_gate_position

    def get_other_gate_position(self):
        return self.__other_gate_position

    def get_real_departure_time(self):
        return self.__real_departure_time

    def get_real_arrival_time(self):
        return self.__real_arrival_time
