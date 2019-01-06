import numpy as np
import matplotlib.pyplot as plt

size = 10
x = np.arange(size)
a = [7,165,89,45,40,24,23,16,12,19]
b = [355,409,342,355,377,381,320,347,359,322]
labels = np.arange(0.05,0.51,0.05)

plt.bar(x, a, label='Detecting slots', hatch="/", tick_label=labels)
plt.bar(x, b, bottom=a, label='Connecting slots', hatch="\\")
plt.xlabel('Duty cycle',fontsize=18)
plt.ylabel('Time slots',fontsize=18)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.legend(loc='best',fontsize=13)
plt.savefig('figure2.eps',bbox_inches='tight')
