import sys
#sys.stdin=open("input.txt","rt")

n,m=map(int, input().split())
l = list(map(int, input().split()))
count = 0

while len(l) != 0:
    ma = []
    for j in range(1,len(l)):
        if m-l[0]>=l[j]:
            ma.append(l[j])
    if len(ma) != 0:
        l.pop(l.index(max(ma)))
    l.pop(0)
    count+=1
            
print(count)