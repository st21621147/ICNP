# -*- coding: utf-8 -*-
from __future__ import  division
import numpy as np
import matplotlib.pyplot as plt


#label = ("Our protocol","pro=0.05","pro=0.1","pro=0.2")
#x =list(range(len(label)))
#list1 = [0.52381,0.285714,0.428571,0.47619]
#list2 = [0.952381,0.380952,0.666667,0.714286]
#list3 = [1,0.904762,0.952381,1]
#total_width, n = 0.9,3
#width = total_width / n
#plt.bar(x, list1, width=width, label="Species I", color="r", hatch="X", align="center")
#for i in range(len(x)):
#    x[i] = x[i] + width
#plt.bar(x, list2, width=width, label="Species II", color="c", hatch="o", align="center")
#for i in range(len(x)):
#    x[i] = x[i] + width
#plt.bar(x, list3, width=width, label="Species III", color="b", hatch="*", align="center")
#
#plt.xticks(np.arange(len(label)), label)
#plt.ylabel("Encounter registration rate", fontsize=16)
#plt.legend(loc='upper right',fontsize=12)
#plt.savefig('figure8.eps', format='eps', bbox_inches='tight')

label = ("Species I","Species II","Species III")
x =list(range(len(label)))
list1 = [0.62381,0.952381,1]
list2 = [0.285714,0.380952,0.904762]
list3 = [0.428571,0.666667,0.952381]
list4 = [0.47619,0.714286,1]
total_width, n = 0.8,4
width = total_width / n
plt.bar(x, list1, width=width, label="Our protocol", color="lightsalmon", edgecolor=['black','black','black','black'], align="center")
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, list2, width=width, label="pro=0.05", color="lightgreen", edgecolor=['black','black','black','black'], align="center")
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, list3, width=width, label="pro=0.1", color="lightskyblue", edgecolor=['black','black','black','black'], align="center")
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, list4, width=width, label="pro=0.2", color="orange", edgecolor=['black','black','black','black'], align="center")

plt.xticks(np.arange(len(label))+0.25, label,fontsize=13)
plt.yticks(fontsize=13)
plt.xlabel('',fontsize=18)
plt.ylabel("Encounter registration rate", fontsize=18)
plt.legend(loc='best',fontsize=12)
plt.savefig('figure8.eps', format='eps', bbox_inches='tight')
