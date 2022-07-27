import numpy as np

x_max = 100
y_max = 50
x_c = 33.33
y_c = 16.67
p1 = (0,0)
p2 = (0,y_max)
p3 = (x_max, 0)
p_c = (x_c,y_c) # center point

# Function that finds the line equation between 2 points
def find_line(x,y):
    co = np.polyfit(x, y, 1)
    a = co[0]
    b = co[1]
    return a,b

x = [0,0]
y = [0,y_max]

print(find_line(x,y))



