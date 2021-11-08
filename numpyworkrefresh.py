import numpy as np  
# a = np.arange (1,10).reshape (3,3)  
# b = np.arange (10,19).reshape (3,3)  
# c = np.dot(a,b)
# e = np.sum(c,axis =0)
# print(e)




# array = np.arange(0,10)
# print(array)


# import numpy as np
# ones =np.ones(9,dtype=bool)
# newones = ones.reshape(3,3)
# print(newones)

# a = np.arange(1,11)

# a[a%2 == 1] = -1 

# print(a)

# a = np.array([0,1,2,3,4,5,6,7,8,9])

# b = a.reshape(2,5)

# print(b)

a = np.arange (1,10).reshape (3,3)  
b = np.arange (10,19).reshape (3,3)  


c = np.dot(a,b)
print(c)

sumofmatrix = np.sum(c)

print(sumofmatrix)

e = np.sum(c,axis =0)

print(e)

e = np.sum(c,axis =1)

print(e)

