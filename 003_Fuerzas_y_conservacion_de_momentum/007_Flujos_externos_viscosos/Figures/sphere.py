import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

data=open('sphere1.dat','r').readlines()
data=np.transpose([np.asarray(x.split(),np.float64) for x in data])

data2=open('sphere2.dat','r').readlines()
data2=np.transpose([np.asarray(x.split(),np.float64) for x in data2])

fig = plt.figure(figsize=(10,6),dpi=300)
ax=fig.add_subplot(111)

plt.grid(True,which='both')
ax.set_axisbelow(True)
plt.yscale('log')
plt.xscale('log')
ax.set_xlim(0.1,10**6)
#ax.set_ylim(.06,400)


#z = np.polyfit(np.log(data2[0]),np.log(data2[1]),10)
#p = np.poly1d(z)
#print(min(data[0]),max(data[0]))
#x=np.linspace(min(data[0]),10**6,10**7)
#y=np.exp(p(np.log(x)))
#y = np.exp(p(np.log(x)))
#print(x)
#ax.plot(x,y)
xst=np.logspace(-1,1)
yst=np.divide(24,xst)
ax.plot(xst,yst,'k--')

f = interp1d(np.log(data2[0]), np.log(data2[1]), kind='cubic')
x=np.linspace(np.log(min(data2[0])),np.log(max(data2[0])),10**7)
#ax.plot(data2[0],data2[1],linewidth=5)
#ax
ax.plot(np.exp(x[1:-1]),np.exp(f(x[1:-1])),'C0',linewidth=2)

ax.plot(data[0],data[1],'C1.')
#ax.plot(x,np.exp(f(np.log(x))))
ax.set_xlabel(r'$Re_D= \frac{\rho V D}{\mu}$',fontsize=20)
ax.set_ylabel(r'$C_D$',fontsize=20)
ax.tick_params(axis='both', which='major', labelsize=15)
ax.text(6,3,r'$C_D=\frac{24}{Re}$',color='k',verticalalignment='top',horizontalalignment='right',fontsize=15,bbox=dict(facecolor='white',edgecolor='none', alpha=0.5))


plt.tight_layout()


plt.savefig('sphere.eps')
plt.savefig('sphere.png')

#plt.show()
