# -*- coding: utf-8 -*-
from .gate_position import GatePosition


class Flight:  # 类似原文件中trip
    def __init__(self,
                 type,
                 scheduledDepartureTime,
                 scheduledArrivalTime,
                 origin: GatePosition,
                 destination: GatePosition,
                 realDepartureTime,
                 realArrivalTime,
                 layover_time):  # 要加ID吗
        # self.id=id #航班号或其它代码
        self.__type = type  # 到港离港 0到港 1离港
        self.__scheduled_departure_time = scheduledDepartureTime  # 预计离开时间
        self.__scheduled_arrival_time = scheduledArrivalTime  # 预计到达时间
        self.__origin = origin  # 出发地
        self.__destination = destination,  # 目的地
        self.__real_departure_time = realDepartureTime  # 实际离开时间，前期用不到
        self.__real_arrival_time = realArrivalTime  # 实际到达时间，前期用不到
        self.__layover_time = layover_time  # 飞机可以停留时间

    def getType(self):  # type到港离港
        return self.__type

    def getLeisureTime(self):
        return self.__layover_time

    def get_layover_time(self):
        return self.__layover_time

    def getScheduledDepartureTime(self):
        return self.__scheduled_departure_time

    def getScheduledArrivalTime(self):
        return self.__scheduled_arrival_time

    def getOrigin(self):
        return self.__origin

    def getDestination(self):
        return self.__destination

    def getRealDepartureTime(self):
        return self.__real_departure_time

    def getRealArrivalTime(self):
        return self.__real_arrival_time
