import sys
#sys.stdin=open("input.txt","rt")

n=int(input())
l=list(map(int,input().split()))
t=[]

avg = round(sum(l)/n)
m=100
for i in range(n):
    d=abs(l[i]-avg)
    if d<m:
        m=d
        k=i
    elif d==m:
        if l[k]<l[i]:
            k=i
print(avg,k+1)