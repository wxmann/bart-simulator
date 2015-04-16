__author__ = 'tangz'

EMBARACADERO = 'Embarcadero'
WEST_OAKLAND = 'West Oakland'
TWELFTH_ST_OAKLAND = '12th St./Oakland'
NINETEENTH_ST_OAKLAND = '19th St./Oakland'
MACARTHUR = 'MacArthur'
ROCKRIDGE = 'Rockridge'
ORINDA = 'Orinda'
LAFAYETTE = 'Lafayette'
WALNUT_CREEK = 'Walnut Creek'
PLEASANT_HILL = 'Pleasant Hill'
CONCORD = 'Concord'
NORTH_CONCORD = 'North Concord/Martinez'
PITTSBURG_BAY_PT = 'Pittsburg/Bay Point'

# numbers from:
# http://www.sfgate.com/bayarea/article/BART-can-t-keep-pace-with-rising-crush-loads-6192950.php
def pittsbaypt():
    pittsbaypt_station = BartStation(PITTSBURG_BAY_PT, 0)
    northconcord_station = BartStation(NORTH_CONCORD, 18, pittsbaypt_station)
    concord_station = BartStation(CONCORD, 32, northconcord_station)
    pleasanthill_station = BartStation(PLEASANT_HILL, 44, concord_station)
    walnutcreek_station = BartStation(WALNUT_CREEK, 62, pleasanthill_station)
    lafayette_station = BartStation(LAFAYETTE, 71, walnutcreek_station)
    orinda_station = BartStation(ORINDA, 79, lafayette_station)
    rockridge_station = BartStation(ROCKRIDGE, 84, orinda_station)
    macarthur_station = BartStation(MACARTHUR, 98, rockridge_station)
    nineteenthoak_station = BartStation(NINETEENTH_ST_OAKLAND, 119, macarthur_station)
    twelfthoak_station = BartStation(TWELFTH_ST_OAKLAND, 120, nineteenthoak_station)
    westoak_station = BartStation(WEST_OAKLAND, 121, twelfthoak_station)
    embarcadero_station = BartStation(EMBARACADERO, 126, westoak_station)
    return BartLine(PITTSBURG_BAY_PT, embarcadero_station)


class BartLine:
    def __init__(self, name, first_station):
        self.name = name
        self.first_station = first_station

    def to_arr(self):
        arr = []
        station = self.first_station
        while station is not None:
            arr.append(station)
            station = station.next_station


class BartStation:
    def __init__(self, name, people, next_station=None):
        self.name = name
        self.people = people
        self.next_station = next_station
