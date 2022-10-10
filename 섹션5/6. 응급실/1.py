import sys
#sys.stdin = open("input.txt", 'r')

n, m=map(int, input().split())
a=list(map(int, input().split()))
cnt=0

while a:
    for j in a:
        if a[0]<j:
            a.append(a.pop(0))
            if m==0:
                m=len(a)-1
            else:
                m-=1
            break
    else:
        a.pop(0)
        cnt += 1
        if m==0:
            print(cnt)
            break
        else:
                m-=1
        