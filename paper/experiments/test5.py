# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def draw(x,y):
    data = pd.read_table('test3.txt',header=0,delim_whitespace=True,index_col=0)
    data.plot();
    
    plt.xlabel(x,fontsize=18)
    plt.ylabel(y,fontsize=18)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.legend(loc='best',fontsize=12)
    plt.savefig('figure5.eps',bbox_inches='tight')
#plt.show()

draw('Time slots','Encounter registration rate')

exit()

