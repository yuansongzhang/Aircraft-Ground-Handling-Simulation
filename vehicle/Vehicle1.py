import common.VehicleArriveEvent
import common.VehicleServiceEvent
import common.VehicleDepartureEvent
import random
import math
class Vehicle1:
    "牵引车类"
    def __init__(self,name,v,x,y,ServiceStatus,PreparationTime,
                 ServiceTime,NextGatePosition,Time,eventList): 
        self.eventList=eventList
        self.Time=Time                              #开始时间
        self.NextGatePosition=NextGatePosition
        self.name=name
        self.v=v                                    #速度
        self.x=x;
        self.y=y;
        self.ServiceStatus=ServiceStatus;           #服务状态
        self.ServiceTime=ServiceTime;               #服务时间
        self.PreparationTime=PreparationTime;       #准备时长
    def run(self,Time):
        self.ServiceStatus=1;                       #在服务
        self.Time=Time;
        
    def finish(self,Time):
        self.ServiceStatus=0;                       #结束服务
        self.Time=Time;
        
    def serviceTime(self):
        self.ServiceTime=random.uniform(10,20);  
        return self.ServiceTime
        
    def distance(self,x,y):
        # x=
        # y=
        self.d=math.sqrt((self.x-x)^2+(self.y-y)^2) #两个x和y没有标明确，也没有写得到机位xy的函数
        
    def generateVehicle1ArrivalGatePositionEvent(self,println):
        event = common.VehicleArrivalGatePositionEvent(Vehicle1)
        self.eventList.add(event)
        self.currentEvent = event
            
    def generateVehicle1ServiceEvent(self,println):
        event = common.VehicleServiceEvent(Vehicle1)
        self.eventList.add(event)
        self.currentEvent = event
        
    def generateVehicle1DepartureGatePositionEvent(self,println):
        event = common.VehicleDepartureGatePositionEvent(Vehicle1)
        self.eventList.add(event)
        self.currentEvent = event
        
    '''
    事件的更新需要写特定的函数吗？（也就是java版本的方法）
    感觉可以直接在事件执行过程中，对车辆的参数和状态进行更新
    '''
        

