# -*- coding: utf-8 -*-

class GatePosition:
    def __init__(self, airport, category, id):
        self.__airport = airport
        self.__category = category  # 0 near gate position, 1 remote gate position
        self.__id = id

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
