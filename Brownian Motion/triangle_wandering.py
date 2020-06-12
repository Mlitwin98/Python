import numpy as np
import random as r
import matplotlib.pyplot as plt


# Do wygenerowania losowego punktu w środku trójkąta o współrzędnych pt1, pt2, pt3
def RandomPointInTriangle(pt1, pt2, pt3):
	s, t = sorted([r.random(), r.random()])
	return s * pt1[0] + (t - s) * pt2[0] + (1 - t) * pt3[0], s * pt1[1] + (t - s) * pt2[1] + (1 - t) * pt3[1]


# Trójkąt
pts = np.array([[0, 0], [1, 0], [0.5, np.sqrt(0.75)]])
triangle = plt.Polygon(pts, fill=False)
ax = plt.gca()
ax.add_patch(triangle)


# Losowy punkt startowy w trójkącie
rnPoint = RandomPointInTriangle((0, 0), (1, 0), (0.5, np.sqrt(0.75)))
pointsX = [rnPoint[0]]
pointsY = [rnPoint[1]]

for i in range(1, 10001):
	rVertex = r.randint(0, 2)
	newX = (pointsX[i-1] + pts[rVertex][0]) / 2
	newY = (pointsY[i-1] + pts[rVertex][1]) / 2
	pointsX.append(newX)
	pointsY.append(newY)

plt.plot(pointsX, pointsY, 'ro')

# PODPISY
plt.title('Błądzenie przypadkowe wewnątrz trójkąta - Autor: Mateusz Litwin')
plt.text(-0.05, 0, 'A', fontsize=17)
plt.text(1, 0, 'B', fontsize=17)
plt.text(0.5, np.sqrt(0.75), 'C', fontsize=17)
# -------

plt.xlim(-0.1, 1.1)
plt.ylim(-0.1, np.sqrt(0.75)+0.1)
plt.show()

# Powstał trójkąt Sierpińskiego
# Jeden z najprostszych fraktali
