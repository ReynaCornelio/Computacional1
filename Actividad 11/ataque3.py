

#Modo cuarentena
# zombie apocalypse modeling
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
plt.ion()
plt.rcParams['figure.figsize'] = 10, 8

P = 0 # birth rate
d = 0.0001 # natural death percent (per day)
B = 0.0095 # transmission percent (per day)
G = 0.0001 # resurect percent (per day)
A = 0.0001 # destroy percent (per day)
poin = 0.3 #poblacion infectada
cuar = 0.0005 #cuarentena
poz= 0.082 #producción de zombies
dead= 0.015 #muertes

# solve the system dy/dt = f(y, t)
def f(y, t):
    Si = y[0]
    Ii = y[1]
    Zi = y[2]
    Ri = y[3]
    Qi = y[4]
    # the model equations (see Munz et al. 2009)
    f0 = P - B*Si*Zi - d*Si
    f1 = B*Si*Zi - poin*Ii - d*Ii - cuar*Ii
    f2 = poin*Ii + G*Ri - A*Si*Zi - poz*Zi
    f3 = d*Si + d*Ii + A*Si*Zi - G*Ri + dead* Qi
    f4 = cuar*Ii + poz*Zi - dead*Qi
    return [f0, f1, f2, f3, f4]

# initial conditions
S0 = 18200. # initial population
I0 = 150
Z0 = 15 # initial zombie population
Q0 = 130
R0 = 0 # 1% of initial pop is dead
y0 = [S0, I0, Z0, R0, Q0]
t = np.linspace(0, 20, 1000) # time grid

# solve the DEs
soln = odeint(f, y0, t)
S = soln[:, 0]
I = soln[:, 1]
Z = soln[:, 2]
R = soln[:, 3]
Q = soln[:, 4]

# plot results
plt.figure()
plt.plot(t, S,"Darkblue", label='Humanos vivos')
plt.plot(t, Z,"pink", label='Zombies')
plt.xlabel('Dias despues del brote')
plt.ylabel('Poblacion')
plt.title('Apocalipsis zombie - Modo cuarentena')
plt.legend(loc=0)