import numpy as np
import matplotlib.pyplot as plt

size = 10
x = np.arange(size)
a = [3,27,24,31,34,30,32,29,31,37]
b = [37,57,116,131,172,227,249,269,292,325]
labels = range(10,101,10)

plt.bar(x, a, label='Detecting slots', hatch="/", tick_label=labels)
plt.bar(x, b, bottom=a, label='Connecting slots', hatch="\\")
plt.xlabel('Number of agents',fontsize=18)
plt.ylabel('Time slots',fontsize=18)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.legend(loc='best',fontsize=13)
plt.savefig('figure1.eps',bbox_inches='tight')
