import numpy as np

# Get the boundary points
boundary_data = np.loadtxt("boundary_points.txt", unpack = True)
top_left_x = min(boundary_data[0])
top_left_y = max(boundary_data[1])
bottom_right_x = max(boundary_data[0])
bottom_right_y = min(boundary_data[1])
print("\ntop_left_x = %f, top_left_y = %f, bottom_right_x = %f, bottom_right_y = %f" %(top_left_x, top_left_y, bottom_right_x, bottom_right_y))

# Mesh size for structured mesh
print("\nMesh size for structured mesh is %f",%(h))
h = 25.0

# Create the mesh
x_intervals = (-top_left_x+bottom_right_x)/h
y_intervals =(-bottom_right_y+top_left_y)/h 
x = np.linspace(top_left_x,bottom_right_x,x_intervals+1)
y = np.linspace(bottom_right_y,top_left_y,y_intervals+1)
xv, yv = np.meshgrid(x,y)

Z = np.full_like(xv,-2.0)

# Decompose into rectangular regions
region1 = [(xv>=-2250) & (xv<=225) & (yv<=1500) & (yv>=200)]
region2 = [(yv<=200) & (yv>=-200) & (xv>=-2250) & (xv<=0)]
region3 = [(xv>=-2250) & (xv<=225) & (yv<=-200) & (yv>=-1500)]
region4 = [(xv>=0) & (xv<=750) & (yv<=150) & (yv>=-150)]
region5 = [(xv>=750) & (xv<=2250) & (yv<=1500) & (yv>=-1500)]
Z[region1] = 5.0
Z[region2] = 5.0
Z[region3] = 5.0
Z[region4] = 5.0
Z[region5] = (-xv[region5] + 1824.5)/214.9

# Write structured mesh to output.txt
dstacked = np.dstack((xv,yv,Z))
with file('output.txt','w') as outfile:
    for slice_2d in dstacked:
        np.savetxt(outfile,slice_2d)

print "\nNew mesh is in output.txt"
