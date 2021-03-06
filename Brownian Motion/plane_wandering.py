import numpy as np
import random as r
import matplotlib.pyplot as plt
colors = ('b', 'g', 'r', 'c', 'm')

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


# Funkcje obliczające J'ty skok dla N'tej cząsteczki
def UnitDistance(N=0, J=1):
	angle = r.uniform(0, 360)
	delX = np.cos(angle)
	delY = np.sin(angle)
	xUnit[N][J] = xUnit[N][J-1] + delX
	yUnit[N][J] = yUnit[N][J-1] + delY


def GaussDistance(N=0, J=1):
	delX = r.gauss(0, 1)
	delY = r.gauss(0, 1)
	xGauss[N][J] = xGauss[N][J-1] + delX
	yGauss[N][J] = yGauss[N][J-1] + delY


def CauchyDistance(N=0, J=1):
	delX = np.tan(-np.pi/2 + np.pi*r.random())
	delY = np.tan(-np.pi/2 + np.pi*r.random())
	xCauchy[N][J] = xCauchy[N][J-1] + delX
	yCauchy[N][J] = yCauchy[N][J-1] + delY
# -----


def BrownianMove(N):
	for i in range(1, J):
		UnitDistance(N, i)
		GaussDistance(N, i)
		CauchyDistance(N, i)


for i in range(N):
	BrownianMove(i)

# PIERWSZY PANEL
plt.figure(figsize=(17, 9))
plt.subplots_adjust(left=0.05, bottom=0.03, right=0.97, top=0.93, wspace=0.13, hspace=0.21)
# Skok jednostkowy plot
plt.subplot(331)
plt.title('Skok jednostkowy')
plt.annotate('START', xy=(0, 0), xytext=(0, 1.3), arrowprops=dict(facecolor='green', shrink=0.05))
plt.annotate('FINISH', xy=(xUnit[0][-1], yUnit[0][-1]), xytext=(xUnit[0][-1], yUnit[0][-1]+1.3), arrowprops=dict(facecolor='red', shrink=0.05))
plt.plot(xUnit[0], yUnit[0])

plt.subplot(332)
plt.title('Średnie x i y w czasie dla skoku jednostkowego')
plt.plot(xUnit.mean(0), 'r-', label='Średnia x')
plt.plot(yUnit.mean(0), 'g--', label='Średnia y')
plt.legend()

plt.subplot(333)
plt.title('Odchylenie standardowe odległości w czasie dla skoku jednostkowego')
plt.plot(np.sqrt(xUnit.std(0)**2 + yUnit.std(0)**2), 'r-')
# ------

# Skok Gauss plot
plt.subplot(334)
plt.title('Skok z rozkładu Gaussa')
plt.annotate('START', xy=(0, 0), xytext=(0, 1.3), arrowprops=dict(facecolor='green', shrink=0.05))
plt.annotate('FINISH', xy=(xGauss[0][-1], yGauss[0][-1]), xytext=(xGauss[0][-1], yGauss[0][-1]+1.3), arrowprops=dict(facecolor='red', shrink=0.05))
plt.plot(xGauss[0], yGauss[0])

plt.subplot(335)
plt.title('Średnie x i y w czasie dla rozkładu Gaussa')
plt.plot(xGauss.mean(0), 'r-', label='Średnia x')
plt.plot(yGauss.mean(0), 'g--', label='Średnia y')
plt.legend()

plt.subplot(336)
plt.title('Odchylenie standardowe odległości w czasie dla rozkładu Gaussa')
plt.plot(np.sqrt(xGauss.std(0)**2 + yGauss.std(0)**2), 'r-')
# ------

# Skok Cauchy plot
plt.subplot(337)
plt.title("Skok z rozkładu Cauch'ego")
plt.annotate('START', xy=(0, 0), xytext=(0, 1.3), arrowprops=dict(facecolor='green', shrink=0.05))
plt.annotate('FINISH', xy=(xCauchy[0][-1], yCauchy[0][-1]), xytext=(xCauchy[0][-1], yCauchy[0][-1]+1.3), arrowprops=dict(facecolor='red', shrink=0.05))
plt.plot(xCauchy[0], yCauchy[0])

plt.subplot(338)
plt.title("Średnie x i y w czasie dla rozkładu Cauchy'ego")
plt.plot(xCauchy.mean(0), 'r-', label='Średnia x')
plt.plot(yCauchy.mean(0), 'g--', label='Średnia y')
plt.legend()

plt.subplot(339)
plt.title("Odchylenie standardowe odległości w czasie dla rozkładu Cauchy'ego")
plt.plot(np.sqrt(xCauchy.std(0)**2 + yCauchy.std(0)**2), 'r-')
# ------

plt.suptitle("Autor: Mateusz Litwin", fontsize=14)
plt.show()

# DRUGI PANEL
plt.figure(figsize=(12, 9))
plt.subplots_adjust(left=0.06, bottom=0.06, right=0.97, top=0.96, wspace=0.17, hspace=0.33)
# Wykresy 5 różnych cząsteczek z kolejnych przypadków
plt.subplot(311)
plt.title("5 cząsteczek o skoku jednostkowym")
for i, color in enumerate(colors):
	plt.plot(xUnit[i], yUnit[i], color, label=f'Cząsteczka nr {i+1}')
plt.legend(loc=2)

plt.subplot(312)
plt.title("5 cząsteczek o skoku z rozkładu Gaussa")
for i, color in enumerate(colors):
	plt.plot(xGauss[i], yGauss[i], color, label=f'Cząsteczka nr {i+1}')
plt.legend(loc=2)

plt.subplot(313)
plt.title("5 cząsteczek o skoku z rozkładu Cauchy'ego")
for i, color in enumerate(colors):
	plt.plot(xCauchy[i], yCauchy[i], color, label=f'Cząsteczka nr {i+1}')
plt.legend(loc=2)
plt.show()
