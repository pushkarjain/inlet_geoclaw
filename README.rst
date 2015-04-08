======
README
======

THe scripts are run in following manner:

#. *loadt.py* generates the 3D scatter plot of the mesh given in *output.txt* (This filename can be changed to visulaize any mesh file of interest). A tooltip feature is provided that allows the user to click the points on the plot and store them in *scratch.txt*. This feature is useful to store the end points that defines the domain of the problem. Once the outer points are selected, *scratch.txt* can be renamed to *boundary_points.txt*.

#. *createmesh.py* uses the *boundary_points.txt* to generate the structured mesh to *output.txt*.


WIth the given set of files, you can run *loadt.py* and *createmesh.py* without any arguments.


Pushkar Kumar Jain
Computational Hydraulics Group
University of Texas at Austin
