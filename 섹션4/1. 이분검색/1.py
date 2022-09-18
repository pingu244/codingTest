import sys
#sys.stdin=open("input.txt","rt")

n,m=map(int,input().split())
l = sorted(list(map(int, input().split())))

s,e=0,len(l)-1
p=(e-s)//2
while l[p] != m:
    if m< l[p]:
        e=p
        p=(e-s)//2
    else:
        s=p
        p=(e-s)//2 + s
print(p+1)