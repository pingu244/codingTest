import sys
#sys.stdin = open("input.txt", 'r')

n, m=map(int, input().split())
a=list(map(int, input().split()))
a=sorted(a)

lt=0
rt=n-1
while lt<=rt:
    p=(lt+rt)//2
    if a[p]<m:
        lt=p+1
    elif a[p]>m:
        rt=p-1
    elif a[p]==m:
        print(p+1)
        break