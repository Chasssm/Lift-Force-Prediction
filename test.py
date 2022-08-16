import numpy as np
from matplotlib import pyplot as plt

'''
Method 1:
from geographiclib.geodesic import Geodesic

number_points = 10

gd = Geodesic.WGS84.Inverse(35, 0, 35, 90)
line = Geodesic.WGS84.Line(gd['lat1'], gd['lon1'], gd['azi1'])

for i in range(number_points + 1):
    point = line.Position(gd['s12'] / number_points * i)
    print((point['lat2'], point['lon2']))
'''

# Define the known points
x = [100, 400]
y = [240, 265]

# Calculate the coefficients. This line answers the initial question. 
coefficients = np.polyfit(x, y, 1)

# Print the findings
a = coefficients[0]
b = coefficients[1]
print(a)
print(b)

# Let's compute the values of the line...
polynomial = np.poly1d(coefficients)
x_axis = np.linspace(0,500,100)
y_axis = polynomial(x_axis)

# ...and plot the points and the line
plt.plot(x_axis, y_axis)
plt.plot( x[0], y[0], 'go' )
plt.plot( x[1], y[1], 'go' )
plt.grid('on')
plt.show()