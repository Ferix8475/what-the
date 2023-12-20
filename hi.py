import matplotlib.pyplot as plt
import numpy as np

def generateHeart(heartParameters, X_OFFSET = 0, Y_OFFSET = 0, theta = 0, color = 'red', outlineColor = 'green', draw = True):

    xParam = heartParameters[0]
    yParam = heartParameters[1]
    radiansTheta = theta
    #radiansTheta = np.radians(theta)

    t = np.linspace(0, 2*np.pi, 1000)

    x = (xParam * np.sin(t)**3 )
    y = yParam * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t) 
    xr = x * np.cos(radiansTheta) - y * np.sin(radiansTheta) + X_OFFSET
    yr = x * np.sin(radiansTheta) + y * np.cos(radiansTheta) + Y_OFFSET
    
    if draw:
        #plt.plot(xr, yr, color = outlineColor, linewidth = 1)
        plt.fill(xr, yr, color = color)

    return xr, yr

def generateCircle(radius, X_OFFSET = 0, Y_OFFSET = 0, color = 'green', outlineColor = 'black', draw = True):

    t = np.linspace(0, 2 * np.pi, 1000)

    x = radius * np.sin(t) + X_OFFSET
    y = radius * np.cos(t) + Y_OFFSET

    if draw:
        #plt.plot(x, y, color = outlineColor, linewidth = 0.5)
        plt.fill(x, y, color = color)

    return x, y

plt.figure()

generateHeart([10, 13], -10, 10, np.pi * 1/4)
generateHeart([10, 13], 10, 10, np.pi * -1/4)
generateHeart([10, 13], -10, -10, np.pi * 3/4)
generateHeart([10, 13], 10, -10, np.pi * -3/4)
generateCircle(8, color = 'yellow')
generateHeart([5, 5], 0,  -2, color = '#FF3385')

t = np.linspace(0, 10 * np.pi, 1000)
stem_x = 0.75 * np.sin(t / 2)
stem_y = -2 * t - 10
plt.plot(stem_x, stem_y, color='green', linewidth=5, label='Curvy Stem (Light Green)')

plt.axis('equal')
plt.axis('off') 
plt.show()

