basics = [int(x) for x in input().split(" ")]
elements = []

for i in range(basics[2]):
    elements += [[int(x) for x in input().split(" ")]]

move = 0
stepCount = 0


def findIndex(elements, i, j):
    for x in range(len(elements)):
        if elements[x][0] == i and elements[x][1] == j:
            return x
    return -1


[i, j] = [int(x) for x in input().split(' ')]

position = findIndex(elements, i, j)
if position != -1:
    print(elements[position][0], " ", elements[position][1], " ", elements[position][2], " ", 1)

while True:

    if move % 2 == 0:
        stepCount += 1

    if move % 4 == 0:  # Go Down !
        
        for x in range(stepCount):
            i += 1
            position = findIndex(elements, i, j)
            if(position != -1):
                print(elements[position][0], " ", elements[position][1], " ", elements[position][0], " ", move % 4 + 1)
        
        if i >= basics[0]:
            break
    
    if move % 4 == 1:  # Go Right !
        
        for x in range(stepCount):
            j += 1
            position = findIndex(elements, i, j)
            if(position != -1):
                print(elements[position][0], " ", elements[position][1], " ", elements[position][0], " ", move % 4 + 1)
        
        if j >= basics[1]:
            break
    
    if move % 4 == 2:  # Go Up !
        
        for x in range(stepCount):
            i -= 1
            position = findIndex(elements, i, j)
            if(position != -1):
                print(elements[position][0], " ", elements[position][1], " ", elements[position][0], " ", move % 4 + 1)
        
        if i < 0:
            break

    if move % 4 == 0:  # Go Left !
        
        for x in range(stepCount):
            j -= 1
            position = findIndex(elements, i, j)
            if(position != -1):
                print(elements[position][0], " ", elements[position][1], " ", elements[position][0], " ", move % 4 + 1)
        
        if j < 0:
            break
    
    move += 1