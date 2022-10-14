import sys
#sys.stdin = open("input.txt", 'r')

n=int(input())
list=list(map(int,input().split()))
avg=round(sum(list)/n)
gap=abs(avg-list[0])
answer=0

for i in range(1, n):
    g=abs(avg-list[i])
    if g<gap:
        gap=g
        answer=i
    elif g==gap:
        if list[answer]<list[i]:
            answer=i
print(avg, answer+1)