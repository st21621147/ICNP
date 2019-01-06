# -*- coding: utf-8 -*-
from __future__ import  division
import numpy as np
import matplotlib.pyplot as plt


#label = ("Our protocol","pro=0.05","pro=0.1","pro=0.2")
#x =list(range(len(label)))
#list1 = [0.3,0.25,0.25,0.2]
#list2 = [0.5,0.45,0.35,0.25]
#list3 = [1,0.65,0.9,0.95]
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
#plt.savefig('figure9_A.eps', format='eps', bbox_inches='tight')

label = ("Species I","Species II","Species III")
x =list(range(len(label)))
list1 = [0.55,0.65,1]
list2 = [0.25,0.45,0.65]
list3 = [0.25,0.35,0.9]
list4 = [0.2,0.25,0.95]
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

plt.xticks(np.arange(len(label))+0.25, label,fontsize=15)
plt.yticks(fontsize=13)
plt.xlabel('',fontsize=18)
plt.ylabel("Encounter registration rate", fontsize=18)
plt.legend(loc='best',fontsize=13)
plt.savefig('figure9_A.eps', format='eps', bbox_inches='tight')
