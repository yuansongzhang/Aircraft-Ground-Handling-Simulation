# -*- coding: utf-8 -*-
from description import Flight
from common import *


class Aircraft:
    def __init__(self,
                 aircraftId,
                 lastGatePosition,
                 lastGatePositionArrivalTimestamp,
                 lastGatePositionDepartureTimestamp,
                 nextGatePosition,
                 nextGatePositionArrivalTimestamp,
                 nextGatePositionDepartureTimestamp,
                 eventList,
                 flight: Flight,
                 ):
        self.__aircraft_id = aircraftId
        self.__last_gate_position = lastGatePosition  # 停机位
        self.__last_gate_position_arrival_timestamp = lastGatePositionArrivalTimestamp
        self.__last_gate_position_departure_timestamp = lastGatePositionDepartureTimestamp
        self.__next_gate_position = nextGatePosition
        self.__next_gate_position_arrival_timestamp = nextGatePositionArrivalTimestamp
        self.__next_gate_position_departure_timestamp = nextGatePositionDepartureTimestamp
        self.__flight = flight
        self.__event_list = eventList
        self.__current_event = None
        self.generate_aircraft_departure_gate_position_event()

    def getAircraftId(self):  # 可以直接调用参数吗？不定义方法
        return self.__aircraft_id

    def getLastGatePosition(self):
        return self.__last_gate_position

    def getLastGatePositionArrivalTimestamp(self):
        return self.__last_gate_position_arrival_timestamp

    def getNextGatePosition(self):
        return self.__next_gate_position

    def getEventList(self):
        return self.__event_list

    def getCurrentEvent(self):
        return self.__current_event

    def getNextGatePositionArrivalTimestamp(self):
        return self.__next_gate_position_arrival_timestamp

    # 生成事件后更新事件

    def generate_aircraft_departure_gate_position_event(self):
        event = AircraftDepartureGatePositionEvent()
        self.__event_list.add(event)
        # update currentEvent.
        self.__current_event = event

    def aircraft_departure_gate_position_event_update(self):
        pass

    def generateAircraftArrivalGatePositionEvent(self):
        pass
        # event = AircraftArrivalGatePositionEvent(self)
        # self.__event_list.add(event)
        # self.currentEvent = event

    def aircraftArrivalGatePositionEventUpdate(self):
        pass
        # #        updates section.
        # self.getLastSection().setRealArrivalTime(self.getNextGatePositionArrivalTimestamp())
        # #        updates the aircraft's parameters.
        # self.__last_gate_position_arrival_timestamp = self.getNextGatePositionArrivalTimestamp()
        # self.__last_gate_position = self.__next_gate_position

    def generateAircraftLayoverGatePositionEvent(self):
        pass
        # event = AircraftLayoverGatePositionEvent(self, println)
        # self.__event_list.add(event)
        # self.currentEvent = event

    def aircraftLayoverGatePositionEventUpdate(self):
        pass

    def generateAircraftFinishingFlightEvent(self):
        pass
        # event = AircraftFinishingFlightEvent(self, println)
        # self.__event_list.add(event)
        # self.currentEvent = event

    def aircraftFinishingTripEventUpdate(self):
        pass
