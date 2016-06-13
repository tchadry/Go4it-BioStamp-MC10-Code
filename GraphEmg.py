import numpy as np
import matplotlib.pyplot as plt
from DataPoint import *


interval_length = 1000.0

"""
  Plot Electromyography Data
"""
data = np.genfromtxt("C:\Users\Jack\PycharmProjects\Go4It Project\Go4It Code\\sprints_front_calf_emg.csv", delimiter=',', skip_header=1, names=['t','v'])
start_ts_ms = np.amin(data['t'])
t = np.subtract(data['t'],start_ts_ms)

start_point = 000000
end_point = 450000



dataPiece = data[start_point:end_point]

data_list = []

current_time = 0
current_point = 0
this_max = -10
this_min = 10
this_sum = 0
for point in data:
    if current_point == 0:
        current_time = point[0] #only want the start time of each interval
    this_max =  min(max(point[1], this_max), 10)
    this_min = max(min(point[1], this_min), -10)
    this_sum = point[1] + this_sum

    current_point += 1.0

    if current_point == interval_length:
        data_list.append(dataPoint(this_max,this_min,this_sum/interval_length, current_time))
        this_max = -10
        this_min = 10
        this_sum = 0
        current_point = 0


y_min = []
for data_point in data_list:
    y_min.append(data_point.get_min())

x_min = []
for data_point in data_list:
    x_min.append(data_point.get_start_time())

y_max = []
for data_point in data_list:
    y_max.append(data_point.get_max())

x_max = []
for data_point in data_list:
    x_max.append(data_point.get_start_time())

fig = plt.figure()
ax1 = fig.add_subplot(111) # Format figure
ax1.set_title('Sprints Front Calf vs Time')
ax1.set_xlabel('Time since Recording Start (ms)')
ax1.set_ylabel('EMG Potential (Volts)')

ax1.plot(x_min, y_min, color='b',linestyle='-',marker='.',alpha=0.7,) #label='EMG Potential (V)')
ax1.plot(x_max, y_max, color='r',linestyle='-',marker='.',alpha=0.7,) #label='EMG Potential (V)')
# ax1.plot(x_min, y_min, 'b--',)
# ax2.plot(x_max, y_max, 'r^')

plt.show() # Draw