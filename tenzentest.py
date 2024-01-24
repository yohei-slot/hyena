import numpy as np 
from scipy.optimize import curve_fit 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 
  
# Generate random 3D data points 
x = np.array([750,750,750,600,600,600,350,350,350,350,-400,-400,-400,-400,-1500,-1500,-1500,-1500,-2000,-2000,-2000])
y = np.array([333,165,0,150,115,40,250,225,150,50,300,250,150,50,300,250,150,50,300,250,150])
z = np.array([0,0,0,0,150,200,0,80,130,230,0,70,160,240,50,110,210,250,50,120,220])
data = np.array([x, y, z]).T 
  
# Define mathematical function for curve fitting 
def func(xy, a, b, c,d, e,f, g): 
    x, y = xy 
    return a + b*x + c*y + d*y**2 + e*x*y - f**(x/g) 
  
# Perform curve fitting 
popt, pcov = curve_fit(func, (x, y), z) 
  
# Print optimized parameters 
print(popt) 
  
# Create 3D plot of the data points and the fitted curve 
fig = plt.figure() 
ax = fig.add_subplot(111, projection='3d') 
ax.scatter(x, y, z, color='blue') 
x_range = np.linspace(0, 1, 50) 
y_range = np.linspace(0, 1, 50) 
X, Y = np.meshgrid(x_range, y_range) 
Z = func((X, Y), *popt) 
ax.plot_surface(X, Y, Z, color='red', alpha=0.5) 
ax.set_xlabel('X') 
ax.set_ylabel('Y') 
ax.set_zlabel('Z') 
plt.show()