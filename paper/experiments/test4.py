# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def draw(x,y):
    data = pd.read_table('test2.txt',header=0,delim_whitespace=True,index_col=0)
    data.plot(style=['o-','s-','^-','x-']);
    
    plt.xlabel(x,fontsize=18)
    plt.ylabel(y,fontsize=18)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.legend(loc='best',fontsize=13)
    plt.savefig('figure4.eps',bbox_inches='tight')
#plt.show()

draw('Duty cycle','Time slots')

exit()
