w = width
h = height
A = Area
AR = Aspect Ratio

The block information format is as follows (for 'n' hard blocks and 'm' soft blocks):

**************************************

hard - <# of hard blocks>
w_1,h_1
w_2,h_2
..
..
..
w_n,h_n

soft - <# of soft blocks>
A_1,ARmin_1,ARmax_1
A_2,ARmin_1,ARmax_1
...
...
...
A_m,ARmin_m,ARmax_m

***************************************

All hard modules are rotatable.


