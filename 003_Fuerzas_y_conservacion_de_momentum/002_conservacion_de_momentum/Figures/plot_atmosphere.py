import numpy as np
import matplotlib.pyplot as plt

data=open('standard_atmosphere.dat','r').readlines()
data=np.transpose([np.asarray(x.split(),np.float) for x in data[2:] if int(x.split()[1])>18000])
data[1]=np.divide(data[1],1000)
data[3]=np.divide(data[3],10**3)
data[5]=np.subtract(data[5],273.15)

plot1=plt.figure(figsize=(6,6),dpi=300)
ax=plot1.add_subplot(111)
ax.plot([-65,40],[0,0],'k--',linewidth=0.5,dashes=(5,5))
ax.plot([-65,40],[11,11],'k--',linewidth=0.5,dashes=(5,5))
ax.plot([-65,40],[20,20],'k--',linewidth=0.5,dashes=(5,5))
ax.plot(data[5],data[1])

plt.xticks(np.arange(-60,40,20),fontsize=15)
plt.yticks(np.arange(0,80,10),fontsize=15)

ax.set_xlim(-65,20)
ax.set_xlabel('Temperatura $(^\circ C)$',fontsize=20)
ax.set_ylabel('Altitud (km)',fontsize=20)
ax.text(-60,5,'Troposfera',fontsize=15)
ax.text(-55,15,'$T=-56.5^\circ$C',fontsize=15)

#plot1.savefig('temperatura_standard.eps')

#########################################

def press_noiso(h):
    p0=101.3 # kPa
    T0=15+273.15
    grb = 5.26
    B = 0.0065
    p = np.multiply(p0,np.power((1-B*h/T0),grb))
    return p

def press_iso(h):
    p0= press_noiso(11000)
    T0=-56.5+273.15 #K
    R = 8.314472 # J / (K mol)
    M = 28.96 * 10**-3 # kg / mol
    g = 9.81 # m/s2
    h0=11000
    p = np.multiply(p0,np.exp(-g*(h-h0)/(R/M)/T0))
    return p

h=np.arange(0,11000,100)
h2=np.arange(11000,20000,100)

p_noiso = press_noiso(h)
p_iso = press_iso(h2)

print(p_iso)
h=np.divide(h,1000)
h2=np.divide(h2,1000)

plot2=plt.figure(figsize=(6,6),dpi=300)
ax2=plot2.add_subplot(111)
ax2.plot([-0.05*10**2,1.05*10**2],[0,0],'k--',linewidth=0.5,dashes=(5,5))
ax2.plot([-0.05*10**2,1.05*10**2],[11,11],'k--',linewidth=0.5,dashes=(5,5))
ax2.plot([-0.05*10**2,1.05*10**2],[20,20],'k--',linewidth=0.5,dashes=(5,5))
ax2.plot(data[3],data[1],'b-')

ax2.plot(p_noiso,h,'b-')
ax2.plot(p_iso,h2,'b-')

plt.xticks(np.arange(0,120,20),fontsize=15)
plt.yticks(np.arange(0,80,10),fontsize=15)

ax2.set_xlim(-5,105)
ax2.set_xlabel('Presión (kPa)',fontsize=20)
ax2.set_ylabel('Altitud (km)',fontsize=20)
ax2.text(0,5,'Troposfera',fontsize=15)
ax2.text(20,15,'$T=-56.5^\circ C$',fontsize=15)
ax2.text(5,50,'$p=1.2$ kPa',fontsize=15)


plot2.savefig('Presion_standard.eps')
