import sys
#sys.stdin=open("input.txt","rt")

n=int(input())
l = list(map(int, input().split()))
m=int(input())

for _ in range(m):
    ma = max(l)
    mi = min(l)
    l[l.index(ma)] = ma-1
    l[l.index(mi)] = mi+1

print(max(l)-min(l))