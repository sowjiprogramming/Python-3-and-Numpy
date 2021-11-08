import numpy as np

d = np.arange(1,11)

d[d%2 == 1] = -1

print(d)