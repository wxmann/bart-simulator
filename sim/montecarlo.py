from collections import OrderedDict
import random
import logging
from sim import exceptions

__author__ = 'tangz'

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# TODO: lazy eval the avg, split into new module that can also calc stdev, etc.
def statistics(simul):
    runs = [result.station_number for result in simul]
    return sum(runs) / len(runs)


def simulation(line, iterations, packing=2, seats=4):
    probs = exit_probabilities(line)
    for i in range(1, iterations+1):
        yield simulate(probs, packing, seats)


def simulate(line_probs, packing, seats):
    logging.info("=================================")
    logging.info("====== STARTING SIMULATION ======")
    logging.info("=================================")
    station_number = 1
    s = seats
    P = packing
    for station, exit_probability in line_probs.items():
        p = exit_probability
        q = (1 - p) ** s
        someone_else_sits = (1 - q) * (P - 1) / P
        i_sit = (1 - q) / P
        someone_else_leaves = 1 - ((1 - p) ** (P - 1))

        x = random.random()
        if x < i_sit:
            logging.info("Finally, I got a seat at {0} station!".format(station.name))
            logging.info("\n")
            return SimulationResult(station.name, station_number)
        elif x < i_sit + someone_else_sits:
            logging.info("At {0} station, someone left his/her seat but someone else took it!".format(station.name))
            P = P - 1 if P >= 2 else 1
        elif x < i_sit + someone_else_sits + someone_else_leaves:
            logging.info(
                "At {0} station, someone standing next to me left, leaving me with a better chance of getting a seat!".format(
                    station.name))
            P = P - 1 if P >= 2 else 1
        else:
            logging.info("Nobody left the train at {0} station.".format(station.name))
        station_number += 1
    raise exceptions.InfiniteBartError('This should not happen!')


# returns probability of person leaving at that station
def exit_probabilities(line):
    probs = OrderedDict()
    station = line.first_station
    while True:
        nextstation = station.next_station
        if nextstation is None:
            break
        if nextstation.next_station is None:
            probs[nextstation] = 1.0
        else:
            this_station_ppl = station.people
            next_station_ppl = nextstation.people
            probs[nextstation] = (this_station_ppl - next_station_ppl) / this_station_ppl
        station = nextstation
    return probs


class SimulationResult:
    def __init__(self, station_name, station_number):
        self.station_name = station_name
        self.station_number = station_number