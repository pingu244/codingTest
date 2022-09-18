import sys
#sys.stdin=open("input.txt","rt")

n=int(input())
l = list(map(int, input().split()))
a=[]

for i in range(n-1,-1,-1):
    if i==n-1:
        a.append(i+1)
        continue
    a.insert(l[i],i+1)
print(*a)