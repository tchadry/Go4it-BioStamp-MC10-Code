import numpy as np
import matplotlib.pyplot as plt
from DataPoint import *


"""
  Plot Accel Data
"""
data = np.genfromtxt("C:\Users\Jack\PycharmProjects\Go4It Project\Go4It Code\\running_chest_accel.csv", delimiter=',', skip_header=1, names=['t','x','y','z'])



start_point = 20000
end_point = 50000



dataPiece = data[start_point:end_point]

timeList = timeIntervalList(0)

current_time = 0
current_max = -10
inRange = False
position = 0

for point in dataPiece:
    if point[2] > 2:
        inRange = True
        new_max =  max(point[2], current_max)
        if new_max > current_max:
            current_time = point[0]
            current_max = new_max

    else:
        if inRange == True:
            timeList.addTime(current_time, position)

        inRange = False
        current_max = -10
        current_time = 0

    position += 1

fig = plt.figure()

ax1 = fig.add_subplot(111) # Format figure
ax1.set_title('Distance of Peaks Chest Acc vs Time')
ax1.set_xlabel('Time since Recording Start (ms)')
ax1.set_ylabel('Distance of Peaks in (ms))')

ax1.plot(timeList.getTimes(), timeList.getTimeIntervals(),color='b',linestyle='None',marker='.',alpha=0.7,) #label='EMG Potential (V)')

leg = ax1.legend()
plt.show() # Draw