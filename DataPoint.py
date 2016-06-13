class dataPoint():
    def __init__(self, max, min, avg, start_time):
        self.max = max
        self.min = min
        self.avg = avg
        self.start_time = start_time

    def get_max(self):
        return self.max

    def get_min(self):
        return self.min

    def get_avg(self):
        return self.avg

    def get_start_time(self):
        return self.start_time


class timeIntervalList():
    times = []
    timeIntervals = []

    def __init__ (self, start_position):
        self.previous_position =  start_position

    def addTime(self, time, position):
        self.times.append(time)
        self.timeIntervals.append(min(position - self.previous_position, 30))
        self.previous_position = position

    def getTimeIntervals(self):
        return self.timeIntervals

    def getTimes(self):
        return self.times
