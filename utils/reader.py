# -*- coding: utf-8 -*-
import pandas as pd
#from description import flight

def generate_flights(filename):
    file = pd.read_excel(filename, encoding = 'utf-8')
    df = pd.DataFrame(file)
    sample = df.sample(n = 1)
    del sample['机型']
    sample.columns = ['航班日期', '航班号', '到港/离港', '机位', '计划到达时间', '实际到达时间', 
                      '计划起飞时间', '实际起飞时间']  
    return sample
