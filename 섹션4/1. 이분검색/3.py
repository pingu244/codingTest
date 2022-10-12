import sys
#sys.stdin = open("input.txt", 'r')

n,m=map(int,input().split())
list=sorted(list(map(int,input().split())))

lp=0
rp=n
p= 0
while m!=list[p]:
    p= (lp+rp)//2
    if m>list[p]:
        lp=p+1
    else:
        rp=p-1
print(p+1)