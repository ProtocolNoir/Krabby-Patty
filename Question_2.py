import numpy as np
r,c,n = (int(x) for x in input().split())
array_sparse = np.arange((n+1)*3).reshape(n+1,3)
array_sparse[0][0],array_sparse[0][1],array_sparse[0][2] = r,c,n
for a in range(1,n+1):
    array_sparse[a][0],array_sparse[a][1],array_sparse[a][2] = (int(x) for x in input().split())
sr, sc = (int(x) for x in input().split())

"""array_big = np.zeros((r,c), int)"""

array_sparse_temp = array_sparse[1:,:]
"""for a in array_sparse_temp:
    tr,tc,tn = a[0],a[1],a[2]
    array_big[tr][tc] = tn"""

def move(m, i, j):
    
    global array_sparse_temp  
    
    if m == 1:
        for a in array_sparse_temp:
            if i == a[0] and j == a[1]:
                print(a[0], a[1], a[2], m)
        i += 1
        return i, j
    elif m == 2:
        for a in array_sparse_temp:
            if i == a[0] and j == a[1]:
                print(a[0], a[1], a[2], m)
        j += 1
        return i, j    
    elif m == 3:
        for a in array_sparse_temp:
            if i == a[0] and j == a[1]:
                print(a[0], a[1], a[2], m)
        i -= 1
        return i, j
    elif m == 4:
        for a in array_sparse_temp:
            if i == a[0] and j == a[1]:
                print(a[0], a[1], a[2],m)
        j -= 1
        return i, j
    
 
def symmetrical_check(m,n):
     if m == n:
         return True, 2*(m-1)
     else:
         return False, m+2
    
def rev_spiral(i,j):
    
    global r,c
    m = r; n = c
    nextmove = 0
    outer = False
    flag = False
    tflag = False
    symmetric, loop = symmetrical_check(m,n)
    
    
    #outer corners
    if i >= 0 and j == 0 and i < m-1:
        nextmove=1
        i -= 1
        j -= 1
        outer = True
                
    if i == 0 and j > 0 and j <= n-1:
        nextmove=4
        i -= 1
        j += 1
        outer = True
            
    if i == m-1 and j >= 0 and j < n-1:
        nextmove=2
        i += 1
        j -= 1
        outer = True
                
    if i <= m-1 and i > 0 and j == n-1:
        nextmove=3 
        i += 1
        j += 1
        outer = True   
                      
        
        
    #inner corners
    if i == int(m/2 - 1) and j == int(n/2 - 1):
        nextmove=1
        i -= 1; j -= 1
        outer = False
                
    if i == int(m/2 - 1) and j == int(n/2):
        nextmove=4
        i -= 1; j += 1
        outer = False
            
    if i == int(m/2) and j == int(n/2 - 1):
        nextmove=2
        i += 1; j -= 1
        outer = False
                
    if i == int(m/2) and j == int(n/2):
        nextmove=3
        i += 1; j += 1
        outer = False                       
    
    
    if outer == True:
        top = left = 0; right = n-1; bottom = m-1
        loop_variable = m 
        tcount = count = -1
    else:
        top = int(m/2 -1); left = int(n/2 -1); right = int(n/2); bottom = int(m/2)
        loop_variable = 1 
        tcount = count = loop
        loop = -1
            
            
    
    #inner loop        
    while(outer == False):
        if count == loop:
            break


        if tcount - count == 2:
            tflag = True
        
        
        if nextmove == 1: #down
            if tflag == True:
                bottom += 1 
            i += 1
            j += 1         
            for a in range(i, bottom+1):
                i, j = move(nextmove, i, j)
            nextmove = 2
            
        elif nextmove == 2: #right
            if tflag == True:
                right += 1
            i -= 1
            j += 1
            for a in range(j,right+1):
                i, j = move(nextmove, i, j)
            nextmove = 3
            
        elif nextmove == 3: #up
            if tflag == True:
                top -= 1
            i -= 1
            j -= 1   
            for a in range(i,top-1, -1):
                i, j = move(nextmove, i, j)
            nextmove = 4
            
        elif nextmove == 4: #left
            if tflag == True:
                left -= 1
            i += 1
            j -= 1     
            for a in range(j,left-1, -1):
                i, j = move(nextmove, i, j)
            nextmove = 1
        
        count -= 1
        
        
    while(outer == True):
        if count == loop:
            break

        if count - tcount == 3:
            tflag = True
        
        
        if nextmove == 1: #down
            if tflag == True:
                bottom -= 1 
            i += 1
            j += 1         
            for a in range(i, bottom+1):
                i, j = move(nextmove, i, j)
            nextmove = 2
            
        elif nextmove == 2: #right
            if tflag == True:
                right -= 1
            i -= 1
            j += 1
            for a in range(j,right+1):
                i, j = move(nextmove, i, j)
            nextmove = 3
            
        elif nextmove == 3: #up
            if tflag == True:
                top += 1
            i -= 1
            j -= 1   
            for a in range(i,top-1, -1):
                i, j = move(nextmove, i, j)
            nextmove = 4
            
        elif nextmove == 4: #left
            if tflag == True:
                left += 1
            i += 1
            j -= 1     
            for a in range(j,left-1, -1):
                i, j = move(nextmove, i, j)
            nextmove = 1
        
        count += 1
          
        

rev_spiral(sr, sc)        