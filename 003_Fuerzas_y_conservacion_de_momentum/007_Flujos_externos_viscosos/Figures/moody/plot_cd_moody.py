import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,8),dpi=300)
ax=fig.add_subplot(111)
plt.grid(True,'both')

ax.set_axisbelow(True)
datas=[200,300,500,1000,2000,5000,10000,20000,50000,200000,1000000]
data_m=[]


def turb_smooth(re):
    return np.divide(0.031,np.power(re,1/7))

def cdlam(re):
    return np.divide(1.33,np.power(re,0.5))

def trans1(re):
    return np.subtract(np.divide(0.031,np.power(re,1/7)),np.divide(1440,re))+0.00006
def trans2(re):
    return np.subtract(np.divide(0.031,np.power(re,1/7)),np.divide(8700,re))+0.00006


def takefirst(elem):
    return elem[0]

x=np.logspace(5,9,1000)

first=True
for i in datas:
    data0=open(str(i)+'.dat').readlines()
    data0=[np.asarray(x.split(),np.float) for x in data0]
    data0=sorted(data0,key=takefirst)
    data0.append([10**9,data0[-1][1]])

    data=[]
    for j in data0[::-1]:
        if j[1]>turb_smooth(j[0]):
            data.append(j)
        else:
            break
    data=sorted(data,key=takefirst)

    data=np.transpose(data)
    data[1]=data[1]+0.00001
    if i<=1000:
        data=list(np.transpose(data))
        data.append([10**5,data[0][1]])
        data=sorted(data,key=takefirst)
        data=np.transpose(data)

    if i>1000:
        xd=np.linspace(10**5,min(data[0]),10)
        yd=turb_smooth(xd)
        inter=np.transpose([xd,yd])
        data=list(np.transpose(data))
        #for i in inter[:-2]:
        #    data.append(i)
        data.append(inter[-3])
        data=sorted(data,key=takefirst)
        data=np.transpose(data)
        #ax.plot(inter)
    #data=np.transpose(list(np.transpose(data)).append(list(inter)))
    data_m.append(data)
    if first:
        ax.text(1.05*10**9,data[1][-1],'$\epsilon/L$ = '+'%1.0e'%(1/i),verticalalignment='center',horizontalalignment='left',fontsize=15)
        first=False
    else:
        ax.text(1.05*10**9,data[1][-1],'%1.0e'%(1/i),verticalalignment='center',horizontalalignment='left',fontsize=15)

    #z=np.polyfit(np.log(data[0]),data[1],3)
    #p=np.poly1d(z)
    ax.plot(data[0],data[1],'C1',label=str(i),linewidth=2)

    #ax.plot(x,p(np.log(x)))

    ax.set_xscale('log')

datar=open('rough.dat').readlines()
datar=[np.asarray(x.split(),np.float) for x in datar]
#datar=sorted(data,key=takefirst)
datar=np.transpose(datar)
datar[1]=datar[1]+0.00008
zr=np.polyfit(np.log(datar[0]),datar[1],6)
pr = np.poly1d(zr)



xtrans=np.logspace(5,8,1000)
cdtrans1=[]
cdtrans2=[]
tol=0.01

for i in x:
    itrans1=trans1(i)
    itrans2=trans2(i)
    ilam=cdlam(i)
    iturb=turb_smooth(i)
    if itrans1>ilam and  itrans1<iturb and abs(itrans1-iturb)/iturb>tol:
        cdtrans1.append([i,itrans1])
    if itrans2>ilam and itrans2<iturb:
        cdtrans2.append([i,itrans2])

cdtrans1=np.transpose(cdtrans1)
cdtrans2=np.transpose(cdtrans2)


ax.set_xlim(10**5,10**9)
ax.set_ylim(0,0.014)
#plt.legend()
ax.set_xlabel(r'$Re_L=\frac{\rho V L}{\mu}$',fontsize=20)
ax.set_ylabel(r'$C_D$',fontsize=20)

xlam=np.logspace(5,7,1000)


ax.tick_params(axis='both', which='major', labelsize=15)


alltrans=[]
xtr1=np.linspace(min(cdtrans1[0]),min(cdtrans2[0]))
for i in xtr1:
    alltrans.append([i,cdlam(i)])
for i in np.transpose(cdtrans2):
    alltrans.append(i)
xtr1=np.linspace(max(cdtrans2[0]),max(cdtrans1[0]))
for i in xtr1:
    alltrans.append([i,turb_smooth(i)])
for i in np.transpose(cdtrans1)[::-1]:
    alltrans.append(i)
alltrans=np.transpose(alltrans)
plt.fill(alltrans[0],alltrans[1],alpha=1,color='white')

ax.plot(cdtrans1[0],cdtrans1[1],'k')
ax.plot(cdtrans2[0],cdtrans2[1],'k')

ax.plot(xlam,cdlam(xlam),'C0',linewidth=3)
ax.plot(x,turb_smooth(x),'C0',linewidth=3)
ax.plot(x,pr(np.log(x)),'C0',dashes=(2,2),linewidth=3)


ax.text(2*10**6,0.002,r'Transición',verticalalignment='center',horizontalalignment='center',fontsize=14)

ax.text(0.51*10**6,0.0105,'Completamente turbulento',verticalalignment='bottom',horizontalalignment='left',fontsize=15,bbox=dict(facecolor='white',edgecolor='none', alpha=0.5))
ax.text(0.85*10**9,0.0012,'Turbulento liso',verticalalignment='center',horizontalalignment='right',fontsize=15,bbox=dict(facecolor='white',edgecolor='none', alpha=0.5))
ax.text(1.2*10**5,0.0012,'Laminar',verticalalignment='center',horizontalalignment='left',fontsize=15,bbox=dict(facecolor='white',edgecolor='none', alpha=0.5))
plt.title('Placa plana paralela al flujo',fontsize=20)

plt.tight_layout()
plt.savefig('moody_cd.eps')
plt.savefig('moody_cd.png')
