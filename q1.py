from collections import OrderedDict 
import numpy as np
d = OrderedDict()
d1 = OrderedDict()
str = "nomatterhowbusyyoumaythinkyouareyoumustfindtimeforreadingorsurrenderyourselftoselfchosenignorance"
for a in str:
    if a not in d:
        d[a] = 1
    else:
        d[a] = d[a] + 1
for a,b in d.items():
    print(a,b, end=' ')
print(" ")
arr1 = []
arr1 = d.keys()
'''arr2 = np.array(d.values())'''
for a in arr1:
    b = d[a]
    d1[b] = d1.get(b,0) + 1
for a,b in d1.items():
    print(a,b)
print(" ")