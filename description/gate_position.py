# -*- coding: utf-8 -*-

class GatePosition:  # 停机位
    def __init__(self, odType, airport, category, id):
        self.__airport = airport  # 所属机场
        self.__category = category  # 远近机位 0近机位，1远机位
        self.__id = id  # 机位号 012345 0近机位，其它远机位

    def get_airport(self):
        return self.__airport

    def getType(self):
        return self.__category

    def getId(self):
        return self.__id

    def setAirport(self, airport):
        self.__airport = airport

    def setType(self, category):
        self.__category = category

    def setId(self, id):
        self.__id = id
