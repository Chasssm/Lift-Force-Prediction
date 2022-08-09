import numpy as np
import matplotlib.pyplot as plt

# 1. Input vertices and center point
x_max = 100
y_max = 50
x_c = 33.33
y_c = 16.67
p1 = (0,0)
p2 = (0,y_max)
p3 = (x_max, 0)
p_c = (x_c,y_c) # center point

# 2. Find the line equations connecting center point and vertices
# Function that finds the line equation between 2 points
# Return y = ax + b
def find_line(p1,p2):
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]
    x = [x1,x2]
    y = [y1,y2]
    coefficients = np.polyfit(x, y, 1)
    a = coefficients[0]
    b = coefficients[1]

    polynomial = np.poly1d(coefficients)
    x_axis = np.linspace(0,500,100)
    y_axis = polynomial(x_axis)

    return a,b
    # plt.plot(x_axis, y_axis)
    # plt.plot( x[0], y[0], 'go' )
    # plt.plot( x[1], y[1], 'go' )
    # plt.grid('on')
    # plt.show()


print(find_line(p1,p2))




# Note: 
# p1[0] is x coor of p1, p1[1] is y coor of p1