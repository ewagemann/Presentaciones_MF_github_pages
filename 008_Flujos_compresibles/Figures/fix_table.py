import numpy as  np

file_name='shock_wave.dat'
file_name='isoentropico.dat'
fback=open(file_name+'back','w')
data=open(file_name,'r').readlines()
data=list([np.asarray(x.split(),np.float) for x in data])


data_mat=[]
data_vect=[]
n=0
for i in data:
    fback.write(str(i[0])+'\n')
    n+=1
    data_vect.append(float(i))
    if n%5==0:
        data_mat.append(data_vect)
        data_vect=[]

fo=open(file_name,'w')
for i in data_mat:
    for j in i:
        fo.write('%12.4f'%j)
    fo.write('\n')
    

    

