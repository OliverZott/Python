'''
Created on 05.05.2019

@author: Oliver Zott

https://matplotlib.org/tutorials/index.html
https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
'''

import matplotlib.pyplot as plt
# import matplotlib
import numpy as np

plt.get_backend()
plt.rcParams["backend"] = "TkAgg"
plt.switch_backend("TkAgg")

fig1 = plt.figure()
fig1.suptitle("No axes on this figure example")

fig1, ax_lst = plt.subplots(2,2)

plt.savefig("fig1.svg", format="svg")



#matplotlib.rcParams['axes.unicode_minus'] = False
plt.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots()
ax.plot(10*np.random.randn(100), 10*np.random.randn(100), 'o')
ax.set_title('Using hyphen instead of Unicode minus')
plt.show()


plt.savefig("test.svg")


x = np.arange(0,100,0.00001)
y = x*np.sin(2*np.pi*x)
plt.plot(y)
plt.savefig("test.svg", format="svg")