import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv

x=np.array([[0.697, 0.46], [0.774, 0.376], [0.634, 0.264], [0.608, 0.318], [0.556,0.215], [0.403,0.237], [0.481,0.149],
           [0.437,0.211], [0.666,0.091], [0.243,0.267], [0.245, 0.057], [0.343, 0.099], [0.639, 0.161], [0.657, 0.198],
           [0.36,0.370], [0.593, 0.042], [0.719,0.103]])
y=np.array([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0])
w = np.array([[0], [0]])
b = np.array([[0]])
x1=[]
x0=[]
for i in range(17):
    if y[i]==1:
        x1.append(x[i])
    else:
        x0.append(x[i])

x0 = np.asarray(x0, dtype=np.float32)
x1 = np.asarray(x1, dtype=np.float32)
# u0=np.array([x[y==0,0]/np.shape(x[y==0,0])[0], x[y==0,1]/np.shape(x[y==0,1])[0]])
# u1=np.array([x[y==1,0]/np.shape(x[y==1,0])[0], x[y==1,1]/np.shape(x[y==1,1])[0]])
u0 = np.sum( x0, axis=0 ) / np.shape( x0 )[0]
u1=np.sum(x1,axis=0)/np.shape(x1)[0]



# print(np.cov(x0.T))
# print(np.matmul((x0-u0).T,(x0-u0))/(np.shape(x0)[0]-1))

Sw=np.cov(x0.T)+np.cov(x1.T)
w=np.matmul(inv(Sw),(u0-u1))
print(w)

plt.scatter(x0[:,0],x0[:,1],marker='*')
plt.scatter(x1[:,0],x1[:,1],marker="o")
plt.xlabel('density')
plt.ylabel('rate of sugar')
plt.xlim(0.1,0.9)
plt.ylim(-0.2,0.4)
plt.plot(x,(np.log(8/9)-w[0]*x)/w[1],color='green')
plt.show()



