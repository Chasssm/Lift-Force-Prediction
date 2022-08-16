import numpy as np
from matplotlib import pyplot as plt

x_max = 200
y_max = 100
s = [2.5, 5, 8, 10]
N = [50, 40, 40, 20]

A = [0,0]
B = [0,y_max]
C = [x_max, 0]
store = []

theta_b = np.arctan(x_max/y_max)
alpha = (np.pi/2-theta_b)/2  # 1/2 theta_c

def get_new_triangle(A, B, C, s):
    delta_b = s/np.tan(theta_b)+s/np.sin(theta_b)
    delta_c = s/np.tan(alpha)
    A1 = [(A[0]+s),(A[1]+s)]
    B1 = [(B[0]+s),(B[1]-delta_b)]
    C1 = [(C[0]-delta_c),(C[1]+s)]
    return [A1, B1, C1]

# print(get_new_triangle(A, B, C, s[0]))

def get_side_line(A, B):
    # Calculate the coefficients
    x = [A[0], B[0]]
    y = [A[1], B[1]]
    coefficients = np.polyfit(x, y, 1)
    
    a = coefficients[0] # Zero Order, Constant Term
    b = coefficients[1] # First Order, Gradient
    co = [a, b]
    return co
    
    # print(a)
    # print(b)            # y = ax + b

    # draw = np.poly1d(coefficients)
    # xs = np.linspace(0,x_max,100)
    # ys = draw(xs)
    # plt.plot(xs, ys)
    # plt.plot( A[0], A[1], 'go' )
    # plt.plot( B[0], B[1], 'go' )
    # plt.grid('on')
    # plt.show()

def get_points(store, A, B, C, N, co):
    Na = int(N/3)
    Nb = int(N/3)
    Nc = int(N/3)    # Adjust later, refer to the ratio of triangle geomerty 
    # On line AB, # of points = Nc
    delta_ab = (B[1] - A[1]) / (Nc + 1)
    d1 = 0
    for i in range(Nc):
        d1 = d1 + delta_ab
        store.append([A[0], (A[1] + d1)])

    # On line AC, # of points = Nb
    delta_ac = (C[0] - A[0]) / (Nb + 1)
    d2 = 0
    for i in range(Nb):
        d2 = d2 + delta_ac
        store.append([(A[0] + d2), A[1]])

    # On line BC, # of points = Na
    delta_x = (C[0] - B[0]) / (Na + 1)   # Increment along x direction
    d3 = B[0]
    for i in range(Na):
        d3 = d3 + delta_x
        store.append([d3, (co[0]*d3 + co[1])])
    
    store = np.array(store)
    return store


for i in range(len(s)):
    new_coor = (get_new_triangle(A, B, C, s[i]))   # return new_coor
    A1 = new_coor[0]
    B1 = new_coor[1]
    C1 = new_coor[2]
    co = get_side_line(B1, C1)
    new_store = get_points(store, A, B, C, N[i], co)

    

# Visualize
x1 = new_store[:,0]
y1 = new_store[:,1]
#plt.figure(figsize = (150, 60))
plt.figure(figsize=(10,5))
plt.plot((0, 0), (0, y_max), scaley = False,c='blue',alpha = 0.75)
plt.plot((x_max, 0),(0, 0),scaley = False,c='blue',alpha = 0.75)
plt.plot((0, x_max), (y_max, 0), scaley = False,c='blue',alpha = 0.75)

# plt.plot((step,(x_max-delta_x)),((y_max-delta_y),step),'m--',label = '2.5 um separation',alpha = 0.75)
# plt.plot((step,step),(step,(y_max-delta_y)),'m--',alpha = 0.75)
# plt.plot((step,(x_max-delta_x)),(step,step),'m--',alpha = 0.75)

plt.scatter(x1,y1,s=20,c='green',edgecolor = 'black',alpha = 0.75)
plt.show


