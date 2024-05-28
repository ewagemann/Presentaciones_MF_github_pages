import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


fig = plt.figure(figsize=(6,7),dpi=300)
ax=fig.add_subplot(111)

plt.grid(True,which='both')
ax.set_axisbelow(True)


data=open('cp_turb.dat','r').readlines()
data=np.transpose([np.asarray(x.split(),np.float64) for x in data])
data2=open('cp_lam.dat','r').readlines()
data2=np.transpose([np.asarray(x.split(),np.float64) for x in data2])

data[0][0]=0
data[1][0]=1
data2[0][0]=0
data2[1][0]=1

data[1]=data[1]+0.02
data2[1]=data2[1]+0.02



xt=np.linspace(0,180,1000)
cpt=1-4*np.power(np.sin(np.multiply(xt,np.pi/180)),2)

f = interp1d(data[0], data[1], kind='cubic')
x=np.linspace(min(data[0]),max(data[0]),2*10**2)

f2 = interp1d(data2[0], data2[1], kind='cubic')
x2=np.linspace(min(data2[0]),max(data2[0]),2*10**2)

ax.plot(xt,cpt,'C0',linewidth=2)
ax.plot(x2[1:-1],f2(x[1:-1]),'C1',linewidth=2)
ax.plot(x[1:-1],f(x[1:-1]),'C2',linewidth=2)
#ax.plot(data[0],data[1],'.')

t=np.linspace(-np.pi,np.pi)
r=20
xc=r*np.cos(t)+90
yc=r*np.sin(t)
yc=np.multiply(yc,(3.2+1.2)/180*6/7)+0.25
x0=[90-r,90]
y0=[0.25,0.25]
y1=[r*np.sin(np.pi/4)*(3.2+1.2)/180*6/7+0.25,0.25]
x1=[r*np.cos(np.pi/4)+90,90]

ax.fill(xc,yc,color='lightgray')
ax.plot(x0,y0,'red')
ax.plot(x1,y1,'red')
ax.plot(xc,yc,'k')

tn=np.linspace(np.pi,np.pi/4)
rn=10
xcn=rn*np.cos(tn)+90
ycn=rn*np.sin(tn)
ycn=np.multiply(ycn,(3.2+1.2)/180*6/7)+0.25
ax.plot(xcn,ycn)
ax.text(90,0.25,r'$\theta$',verticalalignment='bottom',horizontalalignment='right',fontsize=15,bbox=dict(facecolor='none',edgecolor='none', alpha=0.5))
ax.text(105,0.65,r'$Separaci\'on$',verticalalignment='bottom',horizontalalignment='left',fontsize=15,bbox=dict(facecolor='white',edgecolor='none', alpha=0.5))
ax.text(65,0.3,r'$V$',verticalalignment='bottom',horizontalalignment='right',fontsize=15,bbox=dict(facecolor='white',edgecolor='none', alpha=0.5))
ax.text(65,0.2,r'$p_\infty$',verticalalignment='top',horizontalalignment='right',fontsize=15,bbox=dict(facecolor='white',edgecolor='none', alpha=0.5))
ax.text(177,-0.35,'Turbulento',color='C2',verticalalignment='bottom',horizontalalignment='right',fontsize=12,bbox=dict(facecolor='white',edgecolor='none', alpha=0.5))
ax.text(177,-1.05,'Laminar',color='C1',verticalalignment='top',horizontalalignment='right',fontsize=12,bbox=dict(facecolor='white',edgecolor='none', alpha=0.5))
ax.text(177,1.02,'Inviscido',color='C0',verticalalignment='bottom',horizontalalignment='right',fontsize=12,bbox=dict(facecolor='white',edgecolor='none', alpha=0.5))
ax.text(120,-2.5,r'$C_p=1-4\sin^2\theta$',color='C0',verticalalignment='center',horizontalalignment='left',fontsize=12,bbox=dict(facecolor='white',edgecolor='none', alpha=0.5))

#ax.plot(data2[0],data2[1],'.')
# z=np.polyfit(data[0],data[1],20)
# p=np.poly1d(z)
# x=np.linspace(min(data[0]),180,1000)
# ax.plot(x,p(x))
# ax.text((2+7)/2,1.5*0.97,'b',verticalalignment='top',horizontalalignment='center',fontsize=14)
# ax.text(7*1.03,(1.5+1.75)/2,'h',verticalalignment='center',horizontalalignment='left',fontsize=14)

ax.set_ylabel(r'$C_p$',fontsize=20)
ax.set_xlabel(r'$\theta (^\circ)$',fontsize=20)
ax.tick_params(axis='both', which='major', labelsize=15)
ax.set_xticks(np.arange(0,200,20))
ax.set_xlim(0,180)
ax.set_ylim(-3.2,1.2)
#plt.title(r'Distribuci\'on Esfera',fontsize=15)
plt.title(' ',fontsize=15)

plt.tight_layout()


plt.savefig('cp.eps')
plt.savefig('cp.png')
#plt.show()
#plt.show()
