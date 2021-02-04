import numpy as np
import matplotlib.pyplot as plt
def LineFit(x, y):
    '''Returns slope and y-intercept of linear fit to (x,y) data set'''
    xavg = x.mean()
    slope = (y*(x-xavg)).sum()/(x*(x-xavg)).sum()
    yint = y.mean()-slope*xavg
    return slope, yint
x, y = np.loadtxt("1.txt", skiprows=1 , unpack=True)
slope, yint = LineFit(x, y)
x2 = np.array([0, 10])
y2 = slope * x2 + yint
plt.figure(1, figsize = (1,8))
plt.scatter(x, y, color='b', s=20)
plt.plot(x2, y2, color='r', linewidth=3)
plt.axis([0.14,0.25,-232.3,-232])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression\n')
plt.savefig("lin_regression.png")
plt.show()
print(np.corrcoef(x, y))
