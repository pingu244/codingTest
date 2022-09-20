import sys
#sys.stdin=open("input.txt","rt")

n,k=map(int,input().split())
l=list(map(int,input().split()))
t=[]

for i in range(n):
    for j in range(i+1,n):
        for p in range(j+1,n):
            t.append(l[i]+l[j]+l[p])
t=list(set(t))
t.sort(reverse=True)

print(t[k-1])