import sys
#sys.stdin=open("input.txt","rt")

n = int(input())
l1 = list(map(int, input().split()))

m = int(input())
l2= list(map(int, input().split()))

p1=0
p2=0
a=[]

while True:
    if l1[p1]<l2[p2]:
        a.append(l1[p1])
        p1+=1
    else:
        a.append(l2[p2])
        p2+=1
    if p1==n or p2==m:
        break
if p1==n:
    t = l2[p2:]
else:
    t=l1[p1:]
for i in t:
    a.append(i)
print(*a)