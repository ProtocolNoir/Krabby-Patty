import numpy as np
r,c,n = (int(x) for x in input().split())
array_sparse = np.arange((n)*3).reshape(n,3)
for a in range(0,n):
    array_sparse[a][0],array_sparse[a][1],array_sparse[a][2] = (int(x) for x in input().split())
i, j = (int(x) for x in input().split())

def check_element(arr, i, j, c):
    for a in arr:
        if i == a[0] and j == a[1]:
            print(a[0],a[1],a[2],c)
            break


t = 0
d = 1; k = 1
check_element(array_sparse, i, j, d)
t +=1
while t<(r*c):
    for l in range (0,k):
        i += 1
        t += 1
        d = 1
        check_element(array_sparse, i, j, d)
    for l in range (0,k):
        j += 1
        t += 1
        d = 2
        check_element(array_sparse, i, j, d)
    k +=1
    for l in range (0,k):
        i -= 1
        t += 1
        d = 3
        check_element(array_sparse, i, j, d)
    for l in range (0,k):
        j -= 1
        t += 1
        d = 4
        check_element(array_sparse, i, j, d)
    k +=1


