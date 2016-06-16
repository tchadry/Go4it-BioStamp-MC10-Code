from DataPoint import *
import matplotlib.pyplot as plt


class FatigueIndex:

    max_datapoint = 0
    current_fatigue = 100
    data_differences = []
    datapoints = []
    fatigue_over_time = [100]

    def __init__(self,DataPoint):
        self.max_datapoint = DataPoint.get_diff()
        self.datapoints.append(DataPoint)
        self.checkRep()


    def calculateFatigue(self, DataPoint):
        previous_point = self.datapoints[-1]
        proportion = DataPoint.get_diff()/previous_point.get_diff()
        if previous_point.get_diff() > self.max_datapoint:
            self.max_datapoint = previous_point.get_diff()
            self.current_fatigue = 100
        else:
            self.current_fatigue = self.current_fatigue * proportion
        self.fatigue_over_time.append(self.current_fatigue)
        self.data_differences.append(previous_point.get_diff() - DataPoint.get_diff())
        self.checkRep()

    def addDataPoint(self, DataPoint):
        self.calculateFatigue(DataPoint)
        self.datapoints.append(DataPoint)
        self.checkRep()



    def getCurrentFatigue(self):
        return self.current_fatigue

    def displayFatigueGraph(self):
        times_in_seconds = []
        first_time = self.datapoints[0].get_start_time()
        for data_point in self.datapoints:
            times_in_seconds.append((data_point.get_start_time()-first_time)/1000.0) #converts to seconds

        fatigue_fig = plt.figure()
        ax1 = fatigue_fig.add_subplot(111) # Format figure
        ax1.set_title('Fatigue vs Time')
        ax1.set_xlabel('Time (s))')
        ax1.set_ylabel('Fatigue in Percent')

        ax1.plot(times_in_seconds, self.fatigue_over_time, color='b',linestyle='-',marker='.',alpha=0.7,) #label='EMG Potential (V)')

        plt.show() # Draw
        self.checkRep()


    def displayDataPointGraph(self):
        times_in_seconds = []
        first_time = self.datapoints[0].get_start_time()
        for data_point in self.datapoints:
            times_in_seconds.append((data_point.get_start_time()-first_time)/1000.0) #converts to seconds

        data_diff = []
        for data_point in self.datapoints:
            data_diff.append(data_point.get_diff())

        fatigue_fig = plt.figure()
        ax1 = fatigue_fig.add_subplot(111) # Format figure
        ax1.set_title('EMG Max Differences vs Time')
        ax1.set_xlabel('Time (s))')
        ax1.set_ylabel('EMG Potential (volts)')

        ax1.plot(times_in_seconds, data_diff, color='r',linestyle='-',marker='.',alpha=0.7,) #label='EMG Potential (V)')

        plt.show() # Draw
        self.checkRep()

    def checkRep(self):
        assert 0 <= self.current_fatigue <= 100
        assert self.datapoints is not None
