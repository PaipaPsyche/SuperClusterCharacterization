"""
Created on Fri Sep  7 09:48:44 2018

@author: david
"""
import numpy as np
import matplotlib.pyplot as plt
from astropy.convolution import Gaussian2DKernel,convolve

#Data Loading========
data1 = np.loadtxt("Halo3d_Compact.txt")
data1=np.transpose(data1)


VxFile=open("Vx_grid.txt","w")
VyFile=open("Vy_grid.txt","w")
VzFile=open("Vz_grid.txt","w")


X=data1[0]
Y=data1[1]
Z=data1[2]
VX=data1[3]
VY=data1[4]
VZ=data1[5]
M=data1[6]

#======================
L_box  = 1200
n_side = 150
l_side = L_box/n_side
#Dimensiones de la caja (L_box)
#numero de voxeles por dimensión (en el volumen hay n_side ** 3  voxeles)
#lado de cada voxel cúbico (l_side)


delta_m=0.00001  # masa pequeña para evitar divergencia en la división




#Escribiendo el valor de las velocidades
for i in range (n_side):
    print("calculo" , i)
    for j in range (n_side):
        for k in range(n_side):
            min_x = i * l_side
            min_y = j * l_side
            min_z = k * l_side
            ii = (X>min_x) & (X<min_x + l_side) & (Y>min_y) & (Y<min_y+l_side)& (Z>min_z) & (Z<min_z+l_side)
            
            tmp_vx = VX[ii]
            tmp_vy = VY[ii]
            tmp_vz = VZ[ii]
            tmp_m = M[ii]
            
            vx_grid = np.sum(tmp_m * tmp_vx) / (np.sum(tmp_m)+delta_m)
            vy_grid = np.sum(tmp_m * tmp_vy) / (np.sum(tmp_m)+delta_m)
            vz_grid = np.sum(tmp_m * tmp_vz) / (np.sum(tmp_m)+delta_m)
            VxFile.write(str(i)+" "+str(j)+" "+str(k)+" "+str(vx_grid)+"\n")
            VyFile.write(str(i)+" "+str(j)+" "+str(k)+" "+str(vy_grid)+"\n")
            VzFile.write(str(i)+" "+str(j)+" "+str(k)+" "+str(vz_grid)+"\n")
VxFile.close()
VyFile.close()
VzFile.close()
