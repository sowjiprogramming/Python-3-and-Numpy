import numpy as np
a = np.array([1,3,5,6,8,9])
b = np.array([2,5,7,4,12,1])
c = a[(a>=3) & (a<=7)]
print(c)
d = b[(b>=3) & (b<=7)]
print(d)
e = np.concatenate((c,d))
print(e)
sum = np.sum(e)
print(sum)