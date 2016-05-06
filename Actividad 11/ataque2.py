
#Modo infeccion latente 
# zombie apocalypse modeling
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.ion()
plt.rcParams['figure.figsize'] = 10, 8

P = 0 # birth rate
d = 0.00010 # natural death percent (per day)
B = 0.009# transmission percent (per day)
G = 0.0018 # resurect percent (per day)
A = 0.0001# destroy percent (per day)
poin = 0.0015 #poblacion infectada

# solve the system dy/dt = f(y, t)
def f(y, t):
    Si = y[0]
    Ii = y[1]
    Zi = y[2]
    Ri = y[3]
# the model equations (see Munz et al. 2009)
    f0 = P - B*Si*Zi - d*Si
    f1 = B*Si*Zi - poin*Ii - d*Ii
    f2 = poin*Ii + G*Ri - A*Si*Zi
    f3 = d*Si + d*Ii + A*Si*Zi - G*Ri
    return [f0, f1, f2, f3]

# condiciones iniciales 
S0 = 1382. # población inicial
POI = 1 #población infectada pero no convertida
Z0 = 0 # initial zombie population
R0 = 0 # 1% of initial pop is dead
y0 = [S0, POI, Z0, R0]
t = np.linspace(0, 200,10000)# time grid

# solve the DEs
soln = odeint(f, y0, t)
S = soln[:, 0]
I = soln[:, 1]
Z = soln[:, 2]
R = soln[:, 3]

# plot results
plt.figure()
plt.plot(t, S,"Darkblue", label='Humanos vivos')
plt.plot(t, Z,"Orange", label='Zombies')
plt.xlabel('Dias despues del brote')
plt.ylabel('Poblacion')
plt.title('Apocalipsis zombie - Infeccion latente')
plt.legend(loc=0)

