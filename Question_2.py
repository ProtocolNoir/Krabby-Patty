import numpy as np
r,c,n = (int(x) for x in input().split())
array_sparse = np.arange((n+1)*3).reshape(n+1,3)
array_sparse[0][0],array_sparse[0][1],array_sparse[0][2] = r,c,n
for a in range(1,n+1):
    array_sparse[a][0],array_sparse[a][1],array_sparse[a][2] = (int(x) for x in input().split())
print(array_sparse)

array_big = np.zeros((r,c), int)
print(array_big)
