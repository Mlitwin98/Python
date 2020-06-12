import numpy as np
import random as r
import matplotlib.pyplot as plt
# Inicjalizacja X i Y
xUnit = [0]
xGauss = [0]
xCauchy = [0]
yUnit = [0]
yGauss = [0]
yCauchy = [0]


def UnitDistance(i=0):
	angle = r.randint(0, 360)
	delX = np.cos(angle)
	delY = np.sin(angle)
	xUnit.append(xUnit[i] + delX)
	yUnit.append(yUnit[i] + delY)


def GaussDistance(i=0):
	delX = r.gauss(0, 1)
	delY = r.gauss(0, 1)
	xGauss.append(xGauss[i] + delX)
	yGauss.append(yGauss[i] + delY)


def CauchyDistance(i=0):
	delX = np.tan(-np.pi/2 + np.pi*r.random())
	delY = np.tan(-np.pi/2 + np.pi*r.random())
	xCauchy.append(xCauchy[i] + delX)
	yCauchy.append(yCauchy[i] + delY)


def BrownianMove():
	for i in range(10**3):
		UnitDistance(i)
		GaussDistance(i)
		CauchyDistance(i)


BrownianMove()
plt.figure(figsize=(8, 9))
plt.subplots_adjust(left=0.08, bottom=0.03, right=0.96, top=0.96, hspace=0.25)

# Skok jednostkowy plot
plt.subplot(311)
plt.title('Przyrost jednostkowy')
plt.annotate('START', xy=(0, 0), xytext=(0, 1.3), arrowprops=dict(facecolor='green', shrink=0.05))
plt.annotate('FINISH', xy=(xUnit[-1], yUnit[-1]), xytext=(xUnit[-1], yUnit[-1]+1.3), arrowprops=dict(facecolor='red', shrink=0.05))
plt.plot(xUnit, yUnit)
# ------

# Skok Gauss plot
plt.subplot(312)
plt.title('Przyrost z rozkładu Gaussa')
plt.annotate('START', xy=(0, 0), xytext=(0, 1.3), arrowprops=dict(facecolor='green', shrink=0.05))
plt.annotate('FINISH', xy=(xGauss[-1], yGauss[-1]), xytext=(xGauss[-1], yGauss[-1]+1.3), arrowprops=dict(facecolor='red', shrink=0.05))
plt.plot(xGauss, yGauss)
# ------

# Skok Cauchy plot
plt.subplot(313)
plt.title("Przyrost z rozkładu Cauch'ego")
plt.annotate('START', xy=(0, 0), xytext=(0, 1.3), arrowprops=dict(facecolor='green', shrink=0.05))
plt.annotate('FINISH', xy=(xCauchy[-1], yCauchy[-1]), xytext=(xCauchy[-1], yCauchy[-1]+1.3), arrowprops=dict(facecolor='red', shrink=0.05))
plt.plot(xCauchy, yCauchy)
# ------

plt.show()
