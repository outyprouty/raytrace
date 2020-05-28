from math import sqrt

class vec3:

	def __init__(self, x, y, z):
		self.comps = [x,y,z]
	
	def __add__(self, other):
		
		return vec3(*[a+b for a,b in zip(self.comps,other.comps)])

	def __sub__(self, other):
		return vec3(*[a-b for a,b in zip(self.comps,other.comps)])

	def dot(self, other):
		return sum( [a*b for a,b in zip(self.comps,other.comps)] )

	def __mul__(self, scalar):
		return vec3( *[a*scalar for a in self.comps] )

	def getMag(self):
		return sqrt( self.dot(self) )

	def __str__(self):
		return "({},{},{})".format(*self.comps)


class ray:
	
	def __init__(self, start, dir):
		self.start = start
		self.dir = dir

	def getRay(self, t):
		T = vec3(t,t,t)
		return start + dir*T


	def hitSphere(self, sphCent, sphRad):
		tmp = self.start - sphCent
		A = (self.dir).dot(self.dir)
		B = 2*( tmp ).dot(self.dir)
		C = tmp.dot(tmp) - sphRad*sphRad
		discrim = B*B - 4*A*C

		return discrim >= 0



if __name__ == '__main__':
	from sys import argv
	x = float(argv[1])
	origin = vec3(0,0,0)
	direc = vec3(0,1,x)
	sphCent = vec3(0,10,0)
	sphRad = 5
	print(ray(origin, direc).hitSphere(sphCent, sphRad))
			
