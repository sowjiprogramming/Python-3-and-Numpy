import numpy as np

a = np.array([1,2,3])
b = np.r_[np.repeat(a, 3),np.tile(a, 3)]
print(list(b))
d = np.array([1,5,6,8,4,9])
e = np.array([2,4,5,8,10])
f = np.intersect1d(d,e)
print(list(f))
