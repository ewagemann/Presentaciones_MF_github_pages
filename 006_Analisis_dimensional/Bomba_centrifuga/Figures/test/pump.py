#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
#import numpy as np
import scipy.optimize

# Grafico

xmin=0
xmax=26
ymin=0
ymax=40

img = plt.imread("test.png")
y2x=len(img)/(len(img[0]))
fig = plt.figure(dpi=300,figsize=(6,6*y2x))
ax = fig.add_subplot(111)
ax.imshow(img,extent=[xmin,xmax,ymin,ymax],aspect='auto')
ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)


def cole_turb(e_d):
    return (-2*np.log10(e_d/3.7))**-2

def coleb(Re,e_d):
    eqf = lambda f : f**-0.5+2*np.log10(e_d/3.7+2.51/Re/f**0.5)
    ffact = scipy.optimize.newton(eqf,cole_turb(e_d))
    return ffact


g=9.81 # m/s2
mu=0.001 # Pa.s
rho=0.82*10**3 # kg/m3
D=49.75*10**-3 #m
e=1.5*10**-6
e_d=e/D
pa = 150*10**3 # Pa
gamma = rho*g
za = 0
zb = 25
L = 30 #m


def func_vel(v,ktot):
    if v>0:
        Re = rho*v*D/mu
        hl = coleb(Re,e_d)*L/D*v**2/(2*g)
        hlm=v**2/(2*g)*(ktot)
    else:
        hl=0
        hlm=0
    ee = v**2/(2*g) - (pa/gamma + (za-zb) - hl -hlm)


    return ee

Q=np.linspace(0,25,10) # m3/h
v=np.divide(Q,D**2*np.pi/4*3600)#m/s

h=[]
for i in v:
    h.append(func_vel(i,25))
ax.plot(Q,h)
h2=[]
for i in v:
    h2.append(func_vel(i,50))
ax.plot(Q,h2)
#print(h)
plt.savefig('cond.png')
plt.savefig('cond.eps')
