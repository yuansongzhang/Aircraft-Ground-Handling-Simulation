# -*- coding: utf-8 -*-

class GatePosition:  # 停机位
    def __init__(self, odType, airport, type, id):
        # todo, 停机位是固定用于起飞或者到达航班吗?
        self.__odType = odType  # 起止类型，即飞机起飞地Origin，飞机目的地Destination
        self.__airport = airport  # 所属机场
        self.__type = type  # 远近机位 0近机位，1远机位
        self.__id = id  # 机位号 012345 0近机位，其它远机位

    # def getInstance(self):  # 按制定重新进行gateposition
    #     odType = "Origin"
    #     airport = "pudong"
    #     type = 1
    #     id = 1
    #     # print(airport)
    #     return GatePosition(odType, airport, type, id)

    def get_airport(self):
        return self.__airport

    def getType(self):
        return self.__type

    def getId(self):
        return self.__id

    def getODType(self):
        return self.__odType

    def setAirport(self, airport):
        self.__airport = airport

    def setType(self, type):
        self.__type = type

    def setId(self, id):
        self.__id = id

    def setODType(self, odType):
        self.__odType = odType
