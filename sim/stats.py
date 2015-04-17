import matplotlib.pyplot as plt

__author__ = 'tangz'

class Statistics:
    def __init__(self, line, simul):
        self.bartline = line
        self.results = [result.station_number for result in simul]

    def avg_num(self):
        return sum(self.results) / len(self.results)

    def mode(self):
        countmap = {}
        for result in self.results:
            station_name = self.bartline.station(result).name
            existing_count = countmap.get(station_name)
            countmap[station_name] = 0 if existing_count is None else existing_count + 1
        return max(countmap, key=countmap.get)

    # TODO: finish
    def histogram(self):
        plt.bar(range(1, self.bartline.numstations() + 1), self.results)

