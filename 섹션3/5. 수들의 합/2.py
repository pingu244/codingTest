import sys
#sys.stdin=open("input.txt","rt")

n,m=map(int,input().split())
list=list(map(int,input().split()))
cnt = 0
i=0
j=1

while j<n:
    s=0
    for a in range(i,j+1):
        s+=list[a]

    if m<s:
        i+=1
    elif m>s:
        j+=1
    elif m==s:
        cnt+=1
        i+=1
        j+=1
print(cnt)

