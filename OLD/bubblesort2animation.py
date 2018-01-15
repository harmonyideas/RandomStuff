import matplotlib.pyplot as plt
import random
import numpy as np

plt.style.use(['ggplot'])
plt.figure(num=None, figsize=(13, 8), dpi=80, facecolor='w', edgecolor='k')

a_list = random.sample(range(50), 50)

y_pos = np.arange(len(a_list))


swap = True
passes = len(a_list) - 1
while numpasses > 0 and swap:
    swap = False
    # Need to change individual bars instead of clearing current axes
    plt.clf()
    plt.bar(a_list, y_pos, align='center', color='g', alpha=0.5)
    for i in range(numpasses):
        if a_list[i] > a_list[i + 1]:
            swap = True
            temp = a_list[i]
            a_list[i] = a_list[i + 1]
            a_list[i + 1] = temp
    numpasses = numpasses-1

    plt.draw()
    plt.pause(.01)
    # time.sleep(0.001)

# Window will close without this
plt.show()
plt.close()