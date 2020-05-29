from funcs import ray, vec3

from matplotlib import pyplot as plt
from numpy import zeros

img = zeros((2000,2000))

#define camera
camera = vec3(0,0,0)

#define screen top-left location
screenLoc = vec3(-1,10,1)

#define screen physical extent
screenSize = vec3(2,0,2)

#define screen resolution
screenRes = vec3(2000.,0,2000.)

#define screen d's
screenD = (screenSize.x/(screenRes.x), 0, screenSize.z/(screenRes.z))

#cycle through all pixels
for i in range(2000):
	for j in range(2000):
		xPt = screenLoc.x+screenD[0]*i
		yPt = screenLoc.y
		zPt = screenLoc.z-screenD[2]*j
		
		screenPt = vec3(xPt, yPt, zPt)

		#define ray
		r = ray(camera, (screenPt - camera))
		
		#see if ray hits obj
		hits = r.hitSphere(vec3(0,50,1),0.5)
		
		if hits:
			img[i,j] = 100
		else:
			img[i,j] = 0

plt.imshow(img, cmap='gray')
plt.show()
