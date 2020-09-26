from collections import OrderedDict 
d = OrderedDict()
str = "nomatterhowbusyyoumaythinkyouareyoumustfindtimeforreadingorsurrenderyourselftoselfchosenignorance"
for a in str:
    if a not in d:
        d[a] = 1
    else:
        d[a] = d[a] + 1
for a,b in d.items():
    print(a,b, end=' ')
print(" ")
