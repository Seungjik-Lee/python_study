import numpy as np

np1 = np.linspace(0,10,5)
print(np1)

np2 = np.random.randint(0,10,5)
print(np2)

np3 = np.array([1,2,3,10,20])
np4 = np3
np3[2] = 100
print(np4)

np5 = np.array([1,2,3,1,2,3,1,2,3])
print(np.unique(np5))