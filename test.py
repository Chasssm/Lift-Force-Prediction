import numpy as np
from matplotlib import pyplot as plt
from geographiclib.geodesic import Geodesic

number_points = 10

gd = Geodesic.WGS84.Inverse(35, 0, 35, 90)
line = Geodesic.WGS84.Line(gd['lat1'], gd['lon1'], gd['azi1'])

for i in range(number_points + 1):
    point = line.Position(gd['s12'] / number_points * i)
    print((point['lat2'], point['lon2']))