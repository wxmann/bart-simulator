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
def pittsbaypt_sfgate():
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

# numbers from March 2015:
# http://www.bart.gov/about/reports/ridership
def pittsbaypt_official():
    pittsbaypt_station = BartStation(PITTSBURG_BAY_PT, 0)
    northconcord_station = BartStation(NORTH_CONCORD, 3411, pittsbaypt_station)
    concord_station = BartStation(CONCORD, 5221, northconcord_station)
    pleasanthill_station = BartStation(PLEASANT_HILL, 8828, concord_station)
    walnutcreek_station = BartStation(WALNUT_CREEK, 13842, pleasanthill_station)
    lafayette_station = BartStation(LAFAYETTE, 18101, walnutcreek_station)
    orinda_station = BartStation(ORINDA, 20795, lafayette_station)
    rockridge_station = BartStation(ROCKRIDGE, 22972, orinda_station)
    macarthur_station = BartStation(MACARTHUR, 27376, rockridge_station)
    nineteenthoak_station = BartStation(NINETEENTH_ST_OAKLAND, 30019, macarthur_station)
    twelfthoak_station = BartStation(TWELFTH_ST_OAKLAND, 40186, nineteenthoak_station)
    westoak_station = BartStation(WEST_OAKLAND, 43296, twelfthoak_station)
    embarcadero_station = BartStation(EMBARACADERO, 44707, westoak_station)
    return BartLine(PITTSBURG_BAY_PT, embarcadero_station)

class BartLine:
    def __init__(self, name, first_station):
        self.name = name
        self.first_station = first_station
        self.station_arr = self._to_arr()

    def numstations(self):
        return len(self.station_arr)

    def station(self, station_num):
        if station_num <= 0:
            raise ValueError('Station number has to be positive integer!')
        return self.station_arr[station_num - 1]

    def _to_arr(self):
        arr = []
        station = self.first_station
        while station is not None:
            arr.append(station)
            station = station.next_station
        return arr


class BartStation:
    def __init__(self, name, people, next_station=None):
        self.name = name
        self.people = people
        self.next_station = next_station
