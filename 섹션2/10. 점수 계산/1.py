import sys
#sys.stdin=open("input.txt","rt")
    
n = int(input())
nList = list(map(int, input().split()))
score = []

if(nList[0] == 1):
    score.append(1)
else:
    score.append(0)


for i in range(1, n):
    if(nList[i] == 1):
        if (score[i-1] > 0):
            score.append(score[i-1] + 1)
        else:
            score.append(1)
    else:
        score.append(0)

print(sum(score))