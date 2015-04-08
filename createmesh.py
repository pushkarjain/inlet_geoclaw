import numpy as np

boundary_data = np.loadtxt("boundary_points.txt", unpack = True)
h = 25.0

#top left corner of computational domain
top_left_x = min(boundary_data[0])
top_left_y = max(boundary_data[1])

bottom_right_x = max(boundary_data[0])
bottom_right_y = min(boundary_data[1])

print("top_left_x = %f, top_left_y = %f, bottom_right_x = %f, bottom_right_y = %f" %(top_left_x, top_left_y, bottom_right_x, bottom_right_y))

#decompose into rectangular regions


x_intervals = (-top_left_x+bottom_right_x)/h
y_intervals =(-bottom_right_y+top_left_y)/h 
x = np.linspace(top_left_x,bottom_right_x,x_intervals+1)
y = np.linspace(bottom_right_y,top_left_y,y_intervals+1)

xv, yv = np.meshgrid(x,y)
Z = np.full_like(xv,-2.0)
#print xv.shape, yv.shape
#print x_intervals, y_intervals

#region1 = xv[xv>2000]
#print region1

Z[(xv>=-2250) & (xv<=225) & (yv<=1500) & (yv>=200)] = 5.0
Z[(yv<=200) & (yv>=-200) & (xv>=-2250) & (xv<=0)] = 5.0
Z[(xv>=-2250) & (xv<=225) & (yv<=-200) & (yv>=-1500)] = 5.0
Z[(xv>=0) & (xv<=750) & (yv<=150) & (yv>=-150)] = 5.0
#Z[(xv>=750) & (xv<=2250) & (yv<=1500) & (yv>=-1500)] = (-xv+1824.5)/214.9
Z[(xv>=750) & (xv<=2250) & (yv<=1500) & (yv>=-1500)] = (-xv[(xv>=750) & (xv<=2250) & (yv<=1500) & (yv>=-1500)] + 1824.5)/214.9

#print xv,yv,Z
dstacked = np.dstack((xv,yv,Z))
#print dstacked
#print xv.shape, dstacked.shape
#print np.c_[xv, yv, Z]
#np.reshape(dstacked,(xv.shape))
#np.savetxt("hello.out",dstacked,newline='\n')
with file('output.txt','w') as outfile:
    for slice_2d in dstacked:
        np.savetxt(outfile,slice_2d)
#np.savetxt("hello.out",np.c_[xv,yv,Z],newline=" ")
