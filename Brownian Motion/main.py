import numpy as np
import random as r
import matplotlib.pyplot as plt

# ILOSC SKOKOW
J = 1000
# ILOSC CZASTECZEK
N = 100

# Inicjalizacja X i Y
xUnit = np.zeros((N, J))
xGauss = np.zeros((N, J))
xCauchy = np.zeros((N, J))
yUnit = np.zeros((N, J))
yGauss = np.zeros((N, J))
yCauchy = np.zeros((N, J))


def UnitDistance(N=0, i=1):
	angle = r.uniform(0, 360)
	delX = np.cos(angle)
	delY = np.sin(angle)
	xUnit[N][i] = xUnit[N][i-1] + delX
	yUnit[N][i] = yUnit[N][i-1] + delY


def GaussDistance(N=0, i=1):
	delX = r.gauss(0, 1)
	delY = r.gauss(0, 1)
	xGauss[N][i] = xGauss[N][i-1] + delX
	yGauss[N][i] = yGauss[N][i-1] + delY


def CauchyDistance(N=0, i=1):
	delX = np.tan(-np.pi/2 + np.pi*r.random())
	delY = np.tan(-np.pi/2 + np.pi*r.random())
	xCauchy[N][i] = xCauchy[N][i-1] + delX
	yCauchy[N][i] = yCauchy[N][i-1] + delY


def BrownianMove(N):
	for i in range(1, J):
		UnitDistance(N, i)
		GaussDistance(N, i)
		CauchyDistance(N, i)


for i in range(N):
	BrownianMove(i)

plt.figure(figsize=(14, 9))
plt.subplots_adjust(left=0.08, bottom=0.03, right=0.96, top=0.96, hspace=0.25)

# Skok jednostkowy plot
plt.subplot(321)
plt.title('Przyrost jednostkowy')
plt.annotate('START', xy=(0, 0), xytext=(0, 1.3), arrowprops=dict(facecolor='green', shrink=0.05))
plt.annotate('FINISH', xy=(xUnit[0][-1], yUnit[0][-1]), xytext=(xUnit[0][-1], yUnit[0][-1]+1.3), arrowprops=dict(facecolor='red', shrink=0.05))
plt.plot(xUnit[0], yUnit[0])

plt.subplot(322)
plt.title('Średnie x i y w czasie dla przyrostu jednostkowego')
plt.plot(xUnit.mean(0), 'r-', label='Średnia x')
plt.plot(yUnit.mean(0), 'g--', label='Średnia y')
plt.legend()
# ------

# Skok Gauss plot
plt.subplot(323)
plt.title('Przyrost z rozkładu Gaussa')
plt.annotate('START', xy=(0, 0), xytext=(0, 1.3), arrowprops=dict(facecolor='green', shrink=0.05))
plt.annotate('FINISH', xy=(xGauss[0][-1], yGauss[0][-1]), xytext=(xGauss[0][-1], yGauss[0][-1]+1.3), arrowprops=dict(facecolor='red', shrink=0.05))
plt.plot(xGauss[0], yGauss[0])

plt.subplot(324)
plt.title('Średnie x i y w czasie dla rozkładu Gaussa')
plt.plot(xGauss.mean(0), 'r-', label='Średnia x')
plt.plot(yGauss.mean(0), 'g--', label='Średnia y')
plt.legend()
# ------

# Skok Cauchy plot
plt.subplot(325)
plt.title("Przyrost z rozkładu Cauch'ego")
plt.annotate('START', xy=(0, 0), xytext=(0, 1.3), arrowprops=dict(facecolor='green', shrink=0.05))
plt.annotate('FINISH', xy=(xCauchy[0][-1], yCauchy[0][-1]), xytext=(xCauchy[0][-1], yCauchy[0][-1]+1.3), arrowprops=dict(facecolor='red', shrink=0.05))
plt.plot(xCauchy[0], yCauchy[0])

plt.subplot(326)
plt.title("Średnie x i y w czasie dla rozkładu Cauchy'ego")
plt.plot(xCauchy.mean(0), 'r-', label='Średnia x')
plt.plot(yCauchy.mean(0), 'g--', label='Średnia y')
plt.legend()
# ------

plt.show()
