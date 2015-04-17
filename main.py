from functools import partial
from sim import bartdata, montecarlo
import statistics
from sim.stats import Statistics

__author__ = 'tangz'

def main():
    bartline = bartdata.pittsbaypt_official()
    n = 1000
    simul = montecarlo.simulation(bartline, n, packing=2)
    stats = Statistics(bartline, simul)
    print(stats.avg_num())
    print(stats.mode())

if __name__ == "__main__":
    main()
