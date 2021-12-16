import common.VehicleArriveEvent
import common.VehicleServiceEvent
import common.VehicleDepartureEvent
import random
import math
class Vehicle1:
    "牵引车类"
    def __init__(self,name,v,x,y,ServiceStatus,PreparationTime,
                 ServiceTime,NextGate,Time,eventList): 
        self.eventList=eventList
        self.Time=Time
        self.NextGate=NextGate
        self.name=name
        self.v=v
        self.x=x;
        self.y=y;
        self.ServiceStatus=ServiceStatus;           #服务状态
        self.ServiceTime=ServiceTime;               #服务时间
        self.PreparationTime=PreparationTime;       #准备时长
    def run(self,Time):
        self.ServiceStatus=1;
        self.Time=Time;
        
    def finish(self,Time):
        self.ServiceStatus=0;
        self.Time=Time;
        
    def St(self):
        self.ServiceTime=random.uniform(10,20);  
        return self.ServiceTime
        
    def distance(self,x,y):
        self.d=math.sqrt((self.x-x)^2+(self.y-y)^2) 
        
    def generateVehicle1ArrivalEvent(self,println):
        event = common.VehicleArriveEvent(Vehicle1)
        self.eventList.add(event)
        self.currentEvent = event
            
    def generateVehicle1ServiceStationEvent(self,println):
        event = common.VehicleServiceEvent(Vehicle1)
        self.eventList.add(event)
        self.currentEvent = event
        
    def generateAircraftDepartureStationEvent(self,println):
        event = common.VehicleDepartureEvent(Vehicle1)
        self.eventList.add(event)
        self.currentEvent = event
        
    '''
    事件的更新需要写特定的函数吗？（也就是java版本的方法）
    感觉可以直接在事件执行过程中，对车辆的参数和状态进行更新
    '''
        

