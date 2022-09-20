import sys
#sys.stdin=open("input.txt","rt")

n,m=map(int,input().split())
if n<m:
    n,m=m,n

l=[i+2 for i in range(n)]
l=l[m-1:]
print(*l)