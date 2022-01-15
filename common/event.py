# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod, ABC

from aircraft import Aircraft


class Event:
    __meta_class__ = ABCMeta

    def __init__(self):
        self.__triggering_timestamp = None

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass


class AircraftDepartureGatePositionEvent(Event):
    def __init__(self):
        super().__init__()
        self.__aircraft = None
        self.__departure_gate_position = None
        self.__departure_timestamp = None
        self.__next_gate_position_arrival_timestamp = None

    def update(self, aircraft: Aircraft):  # aircraft
        self.__aircraft = aircraft
        # self.__triggering_timestamp = aircraft.getScheduledDepartureTime()

    def execute(self):
        pass
        # #    updates aircraft.
        # self.aircraft.aircraftDepartureStationEventUpdate()
        #
        # #    generates next event.
        # self.aircraft.generateaircraftArrivalStationEvent(self.print)


class AircraftArrivalGatePositionEvent(Event):
    def __init__(self, aircraft, arrivalGatePosition, arrivalTimestamp, lastArrivalTimestamp, println):
        self.aircraft = aircraft  # 航班
        self.arrivalGatePosition = arrivalGatePosition
        self.arrivalTimestamp = arrivalTimestamp
        self.lastArrivalTimestamp = lastArrivalTimestamp
        if self.println == 1:
            print("--------------------------------------------")
            print("Generate " + type(self).__name__)
        self.upate(aircraft)

    # 更新事件
    def update(self):  #
        self.triggeringTimestamp = Aircraft.getNextGatePositionArrivalTimestamp()
        self.arrivalGatePosition = Aircraft.getNextGatePosition();
        self.arrivalTimestamp = self.triggeringTimestamp;
        if self.println == 1:
            self.arrivalGatePosition.info()
            self.aircraft.infoAircraftArrivalGatePositionEvent()

    # 执行事件
    def execute(self):
        #    updates Aircraft.更新航班执行事件
        self.Aircraft.AircraftArrivalGatePositionEventUpdate()

        #    generates next event.生成下一个事件
        self.Aircraft.generateAircraftStoppingGatePositionEvent(self.println)


class AircraftFinishingFlightEvent(Event):
    def __init__(self, aircraft, println):
        self.aircraft = aircraft
        # 还要写什么？？？

        if self.println == 1:
            print("--------------------------------------------")
            print("Generate " + type(self).__name__)
        self.upate(aircraft)

    # 更新事件
    def update(self):  #
        self.triggeringTimestamp = Aircraft.getStoppingStationTimestamp()  # +vehicle???

    # 执行事件
    def execute(self):
        #    updates Aircraft.更新航班执行事件
        self.Aircraft.AircraftFinishingTripEventUpdate()

        #    generates next event.生成下一个事件
        self.Aircraft.generateAircraftStoppingStationEvent(self.println)


class AircraftLayoverGatePositionEvent(Event):

    def __init__(self, stoppingStation):
        self.stoppingStation = stoppingStation

    def AircraftStoppingStationEvent(self, aircraft, println):
        self.println = println
        if self.println == 1:
            print("--------------------------------------------")
            print("Generate " + type(self).__name__)

        self.update(aircraft)

    def update(self, **kwargs):  # aircraft
        pass
        # self.aircraft = aircraft
        # self.triggeringTimestamp = aircraft.getLastStationArrivalTimestamp()
        # self.station = aircraft.getLastStation()
        #
        # if self.println == 1:
        #     self.arrivalStation.info()
        #     self.aircraft.infoAircraftArrivalStationEvent()
        #
        # self.update(self.aircraft)

    def execute(self):
        #    updates Aircraft.
        self.Aircraft.AircraftStoppingStationEventUpdate()

        #    generates next event.
        self.Aircraft.generateAircraftDepartureStationEvent(self.println)


class VehicleArrivalGatePositionEvent(Event):
    "到达事件"

    def __init__(self, vehicle1, sessionStartTimestamp, ArrivalGatePositionTimestamp):
        self.vehicle1 = vehicle1
        self.sessionStartTimestamp = sessionStartTimestamp
        self.ArrivalGatePositionTimestamp = ArrivalGatePositionTimestamp  # 到达机位时间戳如何给？

    def update(self):
        self.sessionStartTimestamp = self.vehicle1.Time  # 开始时间
        self.triggeringTimestamp = self.sessionStartTimestamp
        self.vehicle1.run()

    def execute(self):
        self.ArrivalGatePositionTimestamp += self.vehicle1.PreprationTime


class VehicleDepartureGatePositionEvent(Event):
    "驶离事件"

    def __init__(self, vehicle1, departureTimestamp):
        self.vehicle1 = vehicle1
        self.departureTimestamp = departureTimestamp

    def update(self):
        self.departureTimestamp = VehicleServiceEvent.serviceFinishTimestamp

    def execute(self):
        pass


class VehicleServiceEvent(Event):
    "服务事件"

    def __init__(self, vehicle1, aircraft, serviceStartTimestamp, serviceFinishTimestamp):
        self.vehicle1 = vehicle1
        self.aircraft = aircraft
        self.serviceStartTimestamp = serviceStartTimestamp
        self.serviceFinishTimestamp = serviceFinishTimestamp

    def update(self):
        self.serviceStartTimestamp = self.aircraft.getNextGatePositionArrivalTimestamp()
        self.triggeringTimestamp = self.serviceStartTimestamp

    def execute(self):
        self.vehicle1.finish()
        self.serviceFinishTimestamp = self.serviceStartTimestamp + self.vehicle1.ServiceTime()


class GroundHandlingDispatchEvent(Event):
    def __init__(self):
        super().__init__()

    def update(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        pass


class GroundHandlingWaitingEvent(Event):
    def __init__(self):
        super().__init__()

    def update(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        pass
