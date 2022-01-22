# -*- coding: utf-8 -*-
import pandas as pd
from description import *

def generate_flights(filename):
    file = pd.read_excel(filename)#, encoding = 'utf-8'
    df = pd.DataFrame(file)
    sample = df.sample(n = 1)
    del sample['机型']
    sample.columns = ['航班日期', '航班号', '到港/离港', '机位', 
                      '计划到达时间', '实际到达时间', 
                      '计划起飞时间', '实际起飞时间', 
                      '机位x', '机位y', '机位远近'] 
    print(sample)
    
   
    if sample.iat[0,2] == 'A':
        category = 0
    else:
        category = 1
    
    virtual_gate_position = GatePosition('V', 0, '001', 10, 10)
    
    flight_sample = Flight(category = category, 
                            id = sample.iat[0,1],
                     scheduled_departure_timestamp = sample.iat[0,6],
                     scheduled_arrival_timestamp = sample.iat[0,4],
                     real_departure_timestamp = sample.iat[0,7],
                     real_arrival_timestamp = sample.iat[0,5],
                     local_gate_position = GatePosition('PD',sample.iat[0,10], sample.iat[0,3], sample.iat[0,8], sample.iat[0,9]),
                     other_gate_position = GatePosition('V', 0, '001', 10, 10))
    return flight_sample



