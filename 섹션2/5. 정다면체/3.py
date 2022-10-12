import sys
#sys.stdin = open("input.txt", 'r')

n,m=map(int,input().split())

if n>m:
    n,m=m,n

for i in range(n+1, m+2):
    print(i,end=' ')