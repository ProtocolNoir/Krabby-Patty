import numpy as np
r,c,n = (int(x) for x in input().split())
array_sparse = np.arange((n+1)*3).reshape(n+1,3)
array_sparse[0][0],array_sparse[0][1],array_sparse[0][2] = r,c,n
for a in range(1,n+1):
    array_sparse[a][0],array_sparse[a][1],array_sparse[a][2] = (int(x) for x in input().split())
print(array_sparse)

array_big = np.zeros((r,c), int)

array_sparse_temp = array_sparse[1:,:]
for a in array_sparse_temp:
    tr,tc,tn = a[0],a[1],a[2]
    array_big[tr][tc] = tn
print(array_big)
del array_sparse_temp


def reverse_spiral(m, n, arr) : 
    k = 0; l = 0
      
    # k and m - starting and ending row index 
    # l and n - starting and ending column index 
    # i - iterator  
  
    cnt = 0
    total = m * n 
  
    while (k < m and l < n) : 
        if (cnt == total) : 
            break
  
        # Print the first column from the remaining columns  
        for i in range(k, m) : 
            if arr[i][l] != 0:
                print(arr[i][l], end = " ") 
            cnt += 1
        l += 1
  
        if (cnt == total) : 
            break
  
        # Print the last row from the remaining rows  
        for i in range (l, n) :
            if arr[m-1][i] != 0: 
                print( arr[n-1][i], end = " ") 
            cnt += 1
        m -= 1
          
        if (cnt == total) : 
            break
  
        # Print the last column from the remaining columns  
        if (k < m) : 
            for i in range(n-1, k-1, -1) : 
                if arr[i][n-1] != 0:
                    print(arr[i][n-1], end = " ") 
                cnt += 1
            n -= 1
  
        if (cnt == total) : 
            break
  
        # Print the first row from the remaining rows  
        if (l < n) : 
            for i in range(n-1, l-1, -1) : 
                if arr[k][i] != 0:
                    print( arr[k][i], end = " ") 
                cnt += 1
            k += 1

reverse_spiral(r,c,array_big)