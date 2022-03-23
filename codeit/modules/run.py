# from area import circle, square
# import area as ar
# from area import square as sq

from area import *

from shapes2d import Circle as c
from shapes2d import Square as s

# print(ar.circle(3))
# print(ar.sq(4))

# print(circle(3))
# print(square(4))

sq = s(3)
print(sq.area())

cr = c(2)
print(cr.area())