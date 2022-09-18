import sys
#sys.stdin=open("input.txt","rt")

n = int(input())
nList = list(map(int, input().split()))
answer = 0
avg = round(sum(nList)/n)
gap = abs(nList[0]-avg)

for i in range(1, n):
    now = abs(avg-nList[i])
    if(gap > now):
        gap = now
        answer = i
    elif(gap == now):
        if(nList[answer] < nList[i]):
            answer = i

print ("%d %d" % (avg, answer+1))