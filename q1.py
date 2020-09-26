from collections import OrderedDict 
d = OrderedDict()
str = input()
n = int(input())
freq = list(map(int,input().strip().split()))[:n] 
for a in str:
    if a not in d:
        d[a] = 1
    else:
        d[a] = d[a] + 1
for a,b in d.items():
    print(a,b, end=' ')
print(" ")

d1 = []
for a in freq:
    for i,j in d.items():
        if j == a:
            break
    
