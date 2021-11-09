import numpy as np
from numpy.core.fromnumeric import transpose
np.set_printoptions(formatter={'float': lambda x: "{0:0.6f}".format(x)})


X = np.array([
    [0,0],
    [1,0],
    [2,0],
    [0,1],
    [1,1],
    [2,1],
    [3,1],
    [4,1],
    [5,1],
    [100,1],
    [0,2],
    [1,2],
    [2,2],
    [3,2],
    [4,2],
    [5,2],
    [100,2],
    [3,3],
    [4,3],
    [5,3],
    [100,3]
])

# print(np.transpose(X[1].reshape((1,2))).shape)


sum1 = np.zeros(shape=(2,1))
for i in range(0,17):
    sum1 += np.transpose(X[i].reshape((1,2)))

m1 = (1/17)*sum1

sum2 = np.zeros(shape=(2,1))
for i in range(17,21):
    sum2 += np.transpose(X[i].reshape((1,2)))

m2 = (1/4)*sum2

print("m1: ",m1)
print("m2: ",m2)

s1 = np.zeros(shape=(2,2))
for i in range(0,17):
    s1 += np.matmul(np.transpose(X[i].reshape((1,2)))-m1,np.transpose(np.transpose(X[i].reshape((1,2)))-m1))

s2 = np.zeros(shape=(2,2))
for i in range(17,21):
    s2 += np.matmul(np.transpose(X[i].reshape((1,2)))-m1,np.transpose(np.transpose(X[i].reshape((1,2)))-m1))

S_w = s1 + s2

print("s1: ",s1)
print("s2: ",s2)
print("S_w: ",S_w)

w = np.matmul(np.linalg.inv(S_w),(m2-m1))

print("w: ",w)

S_b = np.matmul(m2-m1, np.transpose(m2-m1))

print("S_b: ",S_b)

numerator = np.matmul(np.matmul(np.transpose(w),S_b),w)
denominator = np.matmul(np.matmul(np.transpose(w),S_w),w)

print("numerator: ",numerator)
print("denominator: ",denominator)