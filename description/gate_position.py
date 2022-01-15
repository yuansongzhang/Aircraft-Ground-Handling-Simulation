# -*- coding: utf-8 -*-

class GatePosition:  # 停机位
    def __init__(self, airport, category, id):
        self.__airport = airport  # 所属机场
        self.__category = category  # 远近机位 0近机位，1远机位
        self.__id = id  # 机位号 012345 0近机位，其它远机位

    def get_airport(self):
        return self.__airport

    def get_category(self):
        return self.__category

    def get_id(self):
        return self.__id

    def set_airport(self, airport):
        self.__airport = airport

    def set_category(self, category):
        self.__category = category

    def set_id(self, id):
        self.__id = id
