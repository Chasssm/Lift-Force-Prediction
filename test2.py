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

print(get_new_triangle(A, B, C, s[0]))