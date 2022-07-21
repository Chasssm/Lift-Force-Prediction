# 1. Basic
# print("Hello World!")

# 2. Format
'''
age = 20
name = 'HM'
print("My age is %d and my name is %s" % (age,name)) # % 表示占位
'''
# 3. Scan ----------- input()
'''
password = input('Enter Password: ')
print('Your Password is: %s' % password)
'''

# 4. import random
import random
Object_list = [
    'Money','Food','Meats',
    'Goods','Wood','Hates'
]
#随机生成其中之一
object = random.choice(Object_list)
guess = input('Enter your guess: ')

if guess == object:
    print('Success!\n')
else:
    print('Fail\n')


'''
def insidetriangle((x1,x2,x3),(y1,y2,y3)):
    import numpy as np
    xs=np.array((x1,x2,x3),dtype=float)
    ys=np.array((y1,y2,y3),dtype=float)

    # The possible range of coordinates that can be returned
    x_range=np.arange(np.min(xs),np.max(xs)+1)
    y_range=np.arange(np.min(ys),np.max(ys)+1)

    # Set the grid of coordinates on which the triangle lies. The centre of the
    # triangle serves as a criterion for what is inside or outside the triangle.
    X,Y=np.meshgrid( x_range,y_range )
    xc=np.mean(xs)
    yc=np.mean(ys)

    # From the array 'triangle', points that lie outside the triangle will be
    # set to 'False'.
    triangle = np.ones(X.shape,dtype=bool)
    for i in range(3):
        ii=(i+1)%3
        if xs[i]==xs[ii]:
            include = X *(xc-xs[i])/abs(xc-xs[i]) > xs[i] *(xc-xs[i])/abs(xc-xs[i])
        else:
            poly=np.poly1d([(ys[ii]-ys[i])/(xs[ii]-xs[i]),ys[i]-xs[i]*(ys[ii]-ys[i])/(xs[ii]-xs[i])])
            include = Y *(yc-poly(xc))/abs(yc-poly(xc)) > poly(X) *(yc-poly(xc))/abs(yc-poly(xc))
        triangle*=include

    # Output: 2 arrays with the x- and y- coordinates of the points inside the
    # triangle.
    return X[triangle],Y[triangle]
'''