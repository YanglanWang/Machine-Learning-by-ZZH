import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv

x=np.array([[0.697, 0.46], [0.774, 0.376], [0.634, 0.264], [0.608, 0.318], [0.556,0.215], [0.403,0.237], [0.481,0.149],
           [0.437,0.211], [0.666,0.091], [0.243,0.267], [0.245, 0.057], [0.343, 0.099], [0.639, 0.161], [0.657, 0.198],
           [0.36,0.370], [0.593, 0.042], [0.719,0.103]])
y=np.array([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0])
w = np.array([[0], [0]])
b = np.array([[0]])
beta = np.concatenate((w,b),axis=0)
# beta=beta[None,:]
m =x.shape[0]

for j in range(100):
    l_1=0
    l_2=0
    # w=beta[0][0:2]
    # b=beta[0][2]
    w=beta[0:2]
    b=beta[2]
    for i in x:
        xi_jian=np.concatenate((i,np.array([1])),axis=None)
        row, column = np.where(x == i)
        p1=np.e**(np.matmul(i,w)+b)/(1+np.e**(np.matmul(i,w)+b))
        p0=1-p1
        l_1=l_1+(-xi_jian*(y[row[0]]-p1))

        #l_2=l_2+np.matmul(i.transpose(),i)*p1*p0
        #l_2=l_2+np.dot( i, i[np.newaxis].T)*p1*p0
        #l_2 = l_2 + np.dot(i, i.reshape((-1,1))) * p1 * p0
        l_2=l_2+np.dot( xi_jian[:, None], xi_jian[None, :])*p1*p0
    beta= beta-np.dot(inv(l_2),l_1[:, None])

# print(beta)

# makers=["*", "o"]
# plt.plot(x, marker=makers[y], c=y)
# plt.scatter(x[:,0],x[:,1],marker=makers[y])
plt.scatter(x[y==0,0],x[y==0,1],marker="*")
plt.scatter(x[y==1,0],x[y==1,1],marker="o")
plt.plot(x, (np.log(8/9)-beta[2,0]-beta[0,0]*x)/beta[1,0],color='red')

plt.xlabel('density')
plt.ylabel('rate of sugar')
plt.xlim(0, 0.8)
plt.ylim(0, 0.5)
plt.show()
