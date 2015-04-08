import numpy as np
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D


#x = np.loadtxt("output.txt", unpack=True)
x = np.loadtxt("boundary_points.txt", unpack=True)
#if os.path.isfile("boundary_points.txt"):
#    os.remove("boundary_points.txt")

def onpick3(event):
    ind = event.ind
    print 'onpick3 scatter:', ind, np.take(x[0], ind), np.take(x[1], ind), np.take(x[2],ind)
    with open("scratch.txt", "a") as f1:
        f1.write(str(np.take(x[0], ind)[0]) + " " + str(np.take(x[1], ind)[0]) +" " + str(np.take(x[2],ind)[0])+"\n")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x[0],x[1],x[2], picker=True)
plt.title("Inlet elevation")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
fig.canvas.mpl_connect('pick_event', onpick3)
plt.show()
