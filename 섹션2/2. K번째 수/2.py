import sys
#sys.stdin=open("input.txt","rt")

t=int(input())
for i in range(t):
    n,s,e,k=map(int,input().split())
    l=list(map(int,input().split()))
    l=sorted(l[s-1:e])
    print("#%d %d" %(i+1,l[k-1]))