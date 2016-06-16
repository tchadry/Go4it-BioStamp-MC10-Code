import numpy as np
import matplotlib.pyplot as plt
from DataPoint import *
from FatigueIndex import *

data = np.genfromtxt("C:\Users\Jack\PycharmProjects\Go4It Project\Go4It Code\\sprints_back_thigh_emg.csv", delimiter=',', skip_header=1, names=['t','v'])

interval_length = 500

start_point = 000000
end_point = 450000
dataPiece = data[start_point:]

data_list = []

current_time = 0
current_point = 0
this_max = -10
this_min = 10
this_sum = 0
for point in dataPiece:
    if current_point == 0:
        current_time = point[0] #only want the start time of each interval
    this_max =  min(max(point[1], this_max), 10)
    this_min = max(min(point[1], this_min), -10)
    this_sum = point[1] + this_sum

    current_point += 1.0

    if current_point == interval_length:
        data_list.append(dataPoint(this_max,this_min,this_max - this_min, this_sum/interval_length, current_time))
        this_max = -10
        this_min = 10
        this_sum = 0
        current_point = 0


previous_increasing = 0
previous_point = None
Fatigue = None

for point in data_list:
    if previous_point == None:
        previous_point = point
        continue
    if point.get_diff() > previous_point.get_diff():
        previous_increasing += 1
    else:
        previous_increasing = 0
    if previous_increasing > 3:
        if Fatigue == None:
            Fatigue = FatigueIndex(point)
        else:
            Fatigue.addDataPoint(point)


#Fatigue.displayFatigueGraph()
Fatigue.displayDataPointGraph()