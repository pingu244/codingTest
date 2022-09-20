import sys
#sys.stdin=open("input.txt","rt")

n=int(input())
l=list(map(int,input().split()))
m = -1
a=0

for i in range(n):
    num=l[i]
    s=0
    while num>0:
        s += num%10
        num = num//10
    if m<s:
        m=s
        a=i
print(l[a])