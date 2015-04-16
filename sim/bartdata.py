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
    return bartline(PITTSBURG_BAY_PT, embarcadero_station)


    # bartline = BartLineStatistics('Pittsburg/Bay Point')
    # bartline.set_people('North Concord/Martinez', 18)
    # bartline.set_people('Concord', 32)
    # bartline.set_people('Pleasant Hill', 44)
    # bartline.set_people('Walnut Creek', 62)
    # bartline.set_people('Lafayette', 71)
    # bartline.set_people('Orinda', 79)
    # bartline.set_people('Rockridge', 84)
    # bartline.set_people('MacArthur', 98)
    # bartline.set_people('19th St./Oakland', 119)
    # bartline.set_people('12th St./Oakland', 120)
    # bartline.set_people('West Oakland', 121)
    # bartline.set_people('Embarcadero', 126)

def bartline(name, begin_station):
    station = begin_station
    stations = []
    while station is not None:
        stations.append(station)
        station = station.next_station
    return stations


class BartStation:
    def __init__(self, name, people, next_station=None):
        self.name = name
        self.people = people
        self.next_station = next_station

# class BartLineStatistics:
#
#     def __init__(self, id):
#         self.ridership = OrderedDict()
#         self.id = id
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if not self.ridership:
#             raise StopIteration("No more stations left!")
#         return self.ridership.popitem()
#
#     def set_people(self, station, people):
#         self.ridership[station] = people
#
#     def get_people(self, station):
#         return self.ridership[station]
#
#     def _total(self):
#         return sum(self.ridership.values())
#
#     def probability(self, station):
#         norm = self._total()
#         if norm == 0:
#             return 0
#         return self.get_people(station) / norm
