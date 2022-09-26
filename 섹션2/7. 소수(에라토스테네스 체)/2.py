import sys
#sys.stdin=open("input.txt","rt")

n=int(input())
l=[0]*(n+1)
cnt = 0

for i in range(2,n+1):
    if l[i]==0:
        cnt += 1
        for j in range(i,n+1,i):
            l[j]=1

print(cnt)