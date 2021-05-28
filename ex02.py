import numpy as np

def doA():
    np1 = np.array([1,5,2,9,10])
    np1.sort()
    print(np1)

def doB():
    np1 = np.array([10,12,1,2,13])
    # 1,2,10,12,13
    np1.sort()
    print(np1[ : : -1])

def doC():
    np1 = np.array([[1,2,3,4,5],[2,4,5,3,8]])
    np1.sort(axis=0)
    print(np1)