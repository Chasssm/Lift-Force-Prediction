import numpy as np
from matplotlib import pyplot as plt

# Function that calculates the AREA of triangle given 3 coordinates
# Using Cross Product
#Hello Yifei
def area(x1,y1,x2,y2,x3,y3):
    return abs((x1 * (y2-y3) + x2 * (y3-y1) + x3 * (y1-y2)) / 2.0)

# Function that checks if a point(x,y) lies inside a triangle
def isInside(x1,y1,x2,y2,x3,y3,x,y):
    err = 1e-6
    A = area (x1, y1, x2, y2, x3, y3) # Total Area
    A1 = area (x, y, x2, y2, x3, y3)
    A2 = area (x1, y1, x, y, x3, y3)
    A3 = area (x1, y1, x2, y2, x, y)
    tmp = A1 + A2 + A3
    if ((A-err)<=tmp<=(A+err)):
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


x_max = 200  # Point (x_max, 0.0)
y_max = 100  # Point (0.0, y_max)a
step = 2.5
store = []

delta_x, delta_y = get_deltas(step, 0, 0, 0, y_max, x_max, 0)

for a in np.arange(0+step, x_max+step-delta_x, step):
    for b in np.arange(0+step, y_max+step-delta_y, step):
        if isInside(step, step, step,y_max-delta_y, x_max-delta_x,step, a,b):
            store.append([a,b])

# Add the corner points
store.append([step, y_max-delta_y])
store.append([x_max-delta_x, step])

store = np.array(store)

p1 = np.array([0,0])
p2 = np.array([0,y_max])
p3 = np.array([x_max,0])

# Function that measures distance from a point p to a line formed by p1 & p2
def dist(p1,p2,p):
    d = abs(np.cross(p2-p1,p-p1)/np.linalg.norm(p2-p1))
    return d

# Function that returns the min distance (from p to 3 lines)
# Returns a value
def min_dist_of_all(p1,p2,p3,p):
    d1 = dist(p1,p2,p)
    d2 = dist(p2,p3,p)
    d3 = dist(p3,p1,p)
    return min(d1,d2,d3)

# Function that returns the max distance (from p to 3 lines)
def max_dist_of_all(p1,p2,p3,p):
    d1 = dist(p1,p2,p)
    d2 = dist(p2,p3,p)
    d3 = dist(p3,p1,p)
    return max(d1,d2,d3)

min_d = []
max_d = []
for i in range(0,len(store)):
    min_d.append(min_dist_of_all(p1,p2,p3,store[i]))
    max_d.append(max_dist_of_all(p1,p2,p3,store[i]))

min_d = np.array(min_d)
max_d = np.array(max_d)

# Function that calculates probability of each point inside "store" array
# Depending on relative positions
# More probaility nearer the edge
def P_xy(store,min_d,max_d):
    prob = []
    for i in range(0,len(store)):
        if min_d[i] == 2.5:
            prob.append(1)
        else:
            prob.append(1-min_d[i]/max_d[i]*0.9)
            
    return prob

P_xy = np.array(P_xy(store,min_d,max_d))

# Generates a random Numpy array with floats [0,1]
rand_Gen = []
for i in range(0,len(store)):
    rand_Gen.append(np.random.random())

# Function that calculates the likelihood of whether a point will exist
# Based on multiplication probability and random factor
def if_exist(P_xy,rand_Gen):
    if_exist = (P_xy>rand_Gen)
    return if_exist

if_exist = np.array(if_exist(P_xy,rand_Gen))

new_store=store[if_exist]

# Visualize
x1 = new_store[:,0]
y1 = new_store[:,1]
#plt.figure(figsize = (150, 60))
plt.figure(figsize=(10,5))
plt.plot((0, 0), (0, y_max), scaley = False,c='blue',alpha = 0.75)
plt.plot((x_max, 0),(0, 0),scaley = False,c='blue',alpha = 0.75)
plt.plot((0, x_max), (y_max, 0), scaley = False,c='blue',alpha = 0.75)

plt.plot((step,(x_max-delta_x)),((y_max-delta_y),step),'m--',label = '2.5 um separation',alpha = 0.75)
plt.plot((step,step),(step,(y_max-delta_y)),'m--',alpha = 0.75)
plt.plot((step,(x_max-delta_x)),(step,step),'m--',alpha = 0.75)

plt.scatter(x1,y1,s=20,c='green',edgecolor = 'black',alpha = 0.75)
plt.show