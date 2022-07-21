import numpy as np

# A function that checks if a point lies inside a trangle
# Calculate the total area formed

def area(x1,y1,x2,y2,x3,y3):
    return abs((x1 * (y1-y3) + x2 * (y3-y1) + x3 * (y1-y2)) / 2.0)

def checkArea(x1,y1,x2,y2,x3,y3,x,y):
    A = area (x1, y1, x2, y2, x3, y3) # Total Area
    A1 = area (x, y, x2, y2, x3, y3)
    A2 = area (x1, y1, x, y, x3, y3)
    A3 = area (x1, y1, x2, y2, x, y)
    if (A == A1 + A2 + A3):
        return True
    else:
        return False

def isInside(x1,y1,x2,y2,x3,y3,x,y):
    if (checkArea(0, 0, 20, 0, 10, 30, 10, 15)):
        # print('Inside')
        return True
    else:
        # print('Not Inside')
        return False

x_max = 50  # Point (x_max, 0.0)
y_max = 50  # Point (0.0, y_max)
a = 0.0    # x coordinate
c = 0
store = []

for a in np.arange(0, 2.5, x_max):
    b = 0.0  # y coordinate
    for b in np.arange(0,2.5, y_max):
        if isInside(0.0,0.0, 0.0,y_max, x_max,0.0, a,b):
            print("Point %d, %d is inside", a, b)
            store[c] = [a,b]
            c = c+1
        else:
            break

d = 0
for d in range(0,c):
    print (store[d])
    print('\n')
    d = d+1





