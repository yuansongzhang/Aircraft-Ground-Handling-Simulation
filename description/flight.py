# -*- coding: utf-8 -*-
from .gate_position import GatePosition


class Flight:  # 类似原文件中trip
    def __init__(self,
                 category,
                 scheduled_departure_time,
                 scheduled_arrival_time,
                 origin: GatePosition,
                 destination: GatePosition,
                 # layover_time
                 ):
        # self.id=id #航班号或其它代码
        self.__category = category  # 到港离港 0到港 1离港
        self.__scheduled_departure_time = scheduled_departure_time  # 预计离开时间
        self.__scheduled_arrival_time = scheduled_arrival_time  # 预计到达时间
        self.__origin = origin  # 出发地
        self.__destination = destination,  # 目的地
        self.__real_departure_time = None  # 实际离开时间，前期用不到
        self.__real_arrival_time = None  # 实际到达时间，前期用不到
        # self.__layover_time = layover_time  # 飞机可以停留时间

    def set_real_departure_time(self, real_departure_time):
        self.__real_departure_time = real_departure_time

    def set_real_arrival_time(self, real_arrival_time):
        self.__real_arrival_time = real_arrival_time

    def get_category(self):  # type到港离港
        return self.__category

    def getLeisureTime(self):
        return self.__layover_time

    def get_layover_time(self):
        return self.__layover_time

    def get_scheduled_departure_time(self):
        return self.__scheduled_departure_time

    def get_scheduled_arrival_time(self):
        return self.__scheduled_arrival_time

    def get_origin(self):
        return self.__origin

    def get_destination(self):
        return self.__destination

    def getRealDepartureTime(self):
        return self.__real_departure_time

    def getRealArrivalTime(self):
        return self.__real_arrival_time
