import matplotlib.pyplot as plt
import numpy as np

datax=[0,25,50,75,100,125,150]
datay=[39,40,39,38,35,32,27]

dataxef=[36.4,49,58,70.4,76.5,84.4,93.6,114.8,124,141.4,149.2,155.6,160]
datayef=[50,60,65,70,72,74,76,78,78,76,74,72,70]

dataxpot=[0,25,50,75,100,125,150]
dataypot=[8,10,12,14.5,17,19,20.5]
dataypot=np.multiply(dataypot,0.7457)

fig=plt.figure(figsize=(7.2,6),dpi=300)
ax=fig.add_subplot(111)
fig.subplots_adjust(right=0.75)
z = np.polyfit(datax,datay,2)
p=np.poly1d(z)
xp=np.linspace(0,175,300)

zef = np.polyfit(dataxef,datayef,2)
pef=np.poly1d(zef)

zpot = np.polyfit(dataxpot,dataypot,3)
ppot = np.poly1d(zpot)

ax.plot(xp,p(xp),'C0')
#ax.plot(datax,datay)
ax.set_yticks(np.arange(0,50,5))
ax.set_xticks(np.arange(0,250,50))

ax.set_xlim(0,200)
ax.set_ylim(0,45)
ax.tick_params(axis='both',labelsize=15)

#############
ax2=ax.twinx()
ax2.set_ylabel('Potencia (kW)',fontsize=20)
ax2.set_ylim(0,20)
ax2.plot(xp,ppot(xp),'C1')
ax2.tick_params(axis='y',labelsize=15)

#############

ax3=ax.twinx()
ax3.set_ylabel('Eficiencia ($\%$)',fontsize=20)
ax3.spines["right"].set_position(("axes", 1.25))
#ax3.set_yticks([-200,2000])
ax3.set_yticks(np.linspace(0,100,5))
ax3.tick_params(axis='y',labelsize=15)
ax3.set_ylim(0,100)

ax3.plot(xp,pef(xp),'C2')
plt.yticks(fontsize=15)


#ax3.set_ylim(-50,20)



ax.text(15,41,'Carga',color='C0',fontsize=18)
ax.text(15,13,'Potencia',color='C1',fontsize=18)
ax.text(15,35,'Eficiencia',color='C2',fontsize=18)

ax.set_ylabel('Carga total (m)',fontsize=20)
ax.set_xlabel('Capacidad (m$^3$/h)',fontsize=20)
plt.tight_layout()
plt.savefig('curva_bomba.eps')
plt.savefig('curva_bomba.png')
#pltplt.show()
