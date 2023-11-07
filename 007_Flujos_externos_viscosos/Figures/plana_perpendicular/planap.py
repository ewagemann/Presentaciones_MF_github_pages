import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

data=open('plana.dat','r').readlines()
data=np.transpose([np.asarray(x.split(),np.float64) for x in data])

rect=[[2,1.5],[7,1.5],[7,1.75],[2,1.75],[2,1.5]]
rect=np.transpose(rect)

fig = plt.figure(figsize=(6,4),dpi=300)
ax=fig.add_subplot(111)

plt.grid(True,which='both')
ax.set_axisbelow(True)


z=np.polyfit(data[0],data[1],2)
p=np.poly1d(z)
x=np.linspace(min(data[0]),20,1000)
ax.plot(x,p(x))
ax.fill(rect[0],rect[1],alpha=1,color='gray')
ax.plot(rect[0],rect[1],'k')
ax.text((2+7)/2,1.5*0.97,'b',verticalalignment='top',horizontalalignment='center',fontsize=14)
ax.text(7*1.03,(1.5+1.75)/2,'h',verticalalignment='center',horizontalalignment='left',fontsize=14)

ax.set_xlabel(r'$b/h$',fontsize=20)
ax.set_ylabel(r'$C_D$',fontsize=20)
ax.tick_params(axis='both', which='major', labelsize=15)
ax.set_xticks(np.arange(0,22,2))
ax.set_xlim(0,20)
ax.set_ylim(0.5,2)
plt.title(r'Placa plana perpendicular al flujo ($Re>1000$)',fontsize=15)
plt.tight_layout()

plt.savefig('planap.eps')
plt.savefig('planap.png')

#plt.show()
