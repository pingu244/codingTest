import sys
#sys.stdin=open("input.txt","rt")

n=int(input())
l=list(map(str,input().split()))
m = -1
a=0

for i in range(n):
    num=l[i]
    s=0
    while num:
        s += int(num[-1])
        num = num[:-1]
    if m<s:
        m=s
        a=i
print(l[a])