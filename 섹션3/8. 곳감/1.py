import sys
#sys.stdin=open("input.txt","rt")

n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

m = int(input())
for _ in range(m):
    row, dir, num = map(int, input().split())
    if dir==1:
        w = n-(num%n)
    else:
        w = num%n
    temp = l[row-1][:w]
    l[row-1] = l[row-1][w:]
    l[row-1] = l[row-1] + temp

count = 0
for i in range(n+1//2):
    for j in range(i,n-i):
        count += l[i][j]
        if i !=(n+1)//2-1:
            count += l[n-i-1][j]

print(count)