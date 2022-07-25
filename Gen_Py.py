import numpy as np

# Function that calculates the AREA of triangle given 3 coordinates
# Using Cross Product
def area(x1,y1,x2,y2,x3,y3):
    return abs((x1 * (y2-y3) + x2 * (y3-y1) + x3 * (y1-y2)) / 2.0)

# Function that checks if a point(x,y) lies inside a triangle
def isInside(x1,y1,x2,y2,x3,y3,x,y):
    A = area (x1, y1, x2, y2, x3, y3) # Total Area
    A1 = area (x, y, x2, y2, x3, y3)
    A2 = area (x1, y1, x, y, x3, y3)
    A3 = area (x1, y1, x2, y2, x, y)
    tmp = A1 + A2 + A3
    tmp2 = tmp==A
    if (A == A1 + A2 + A3):
        return True
    else:
        return False

# Function that calculates the acute angle at the vertices
def get_acute_angles(x1, y1, x2, y2, x3, y3):
    H = ((x3-x1)**2 + (y2-y1)**2)**(1/2)
    theta_123 = np.arcsin((x3-x1)/H)
    theta_132 = np.arcsin((y2-y1)/H)
    
    return theta_123, theta_132

# Function that measures the new coordinates
# By deducting delta_x and delta_y from the original ones
def get_deltas(step, x1, y1, x2, y2, x3, y3):
    theta_123, theta_132 = get_acute_angles(x1, y1, x2, y2, x3, y3)
    
    delta_x = step / np.tan(theta_132/2)
    delta_y = step / np.tan(theta_123/2)
    
    return delta_x, delta_y


def fn():

    x_max = 50  # Point (x_max, 0.0)
    y_max = 50  # Point (0.0, y_max)a
    step = 2.5
    store = []

    delta_x, delta_y = get_deltas(step, 0, 0, 0, y_max, x_max, 0)

    for a in np.arange(0+step, x_max+step-delta_x, step):
        for b in np.arange(0+step, y_max+step-delta_y, step):
            if isInside(step, step, step,y_max-delta_y, x_max-delta_x,step, a,b):
                store.append([a,b])


    store.append([step, y_max-delta_y])
    store.append([x_max-delta_x, step])
    return store


if __name__ == '__main__':
    print(fn())
