import sys
#sys.stdin=open("input.txt","rt")
    
n = int(input())
answer = 0

for i in range(n):
    temp = 0
    nList = list(map(int, input().split()))
    newList = []
    for j in nList:
        if j not in newList:
            newList.append(j)
        else:
            value = list(set(nList))
            if(len(value) > 1):
                temp = 1000+ j *100
            else:
                temp = 10000 + j*1000
            break
        if (len(newList) == 3):
                temp = max(nList) * 100   

    if(answer < temp):
        answer = temp

print(answer)