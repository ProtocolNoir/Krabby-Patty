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

tally = []
tempdict = OrderedDict()
tally = d.keys()
for a in tally:
    t = tempdict.get(d[a],0) + 1
    tempdict[d[a]] = t

d1 = d.copy()
flag = 0
for a in freq:
    t = tempdict[a]
    check = 0
    for i,j in d.items():
        if j == a and flag == 0:
            flag = 1
            check = check +1
        elif j == a and flag == 1 and check == t-1:
            flag = 0
            check = check +1
        elif flag == 1:
            if j<a:
                d1.move_to_end(i, last=False)
            elif j>a:
                d1.move_to_end(i)
            elif j == a:
                check = check +1
    for a,b in d1.items():
        print(a,b, end=' ')
    print(" ")
    d.clear()
    d = d1.copy()
    flag = 0
        
