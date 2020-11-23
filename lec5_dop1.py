from sympy import symbols
from sympy import sqrt
from sympy.vector import CoordSys3D
from sympy import sin, cos, trigsimp
from sympy import simplify, expand, factor
A = CoordSys3D('A')
a = 4*A.i + 3*A.j + 8*A.k
b = -2*A.i + 8*A.j + 7*A.k
c = -5*A.i - 6*A.j + 12*A.k
a1 = a.magnitude()
b1 = b.magnitude()
c1 = c.magnitude()
Q = a.dot(b)
W = a.dot(c)
E = b.dot(c)
cos_ab = Q/(a1*b1)
cos_ac = W/(b1*c1)
cos_bc = E/(c1*b1)
print(cos_ac)
print(cos_bc)
print(cos_ab)