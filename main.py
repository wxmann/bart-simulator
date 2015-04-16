from functools import partial
from sim import bartdata, montecarlo

__author__ = 'tangz'

def main():
    bartline = bartdata.pittsbaypt()
    n = 1000
    process = montecarlo.simulation(bartline, n)
    print(montecarlo.statistics(process))

if __name__ == "__main__":
    main()
