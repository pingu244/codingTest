import sys
#sys.stdin=open("input.txt","rt")

n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
count = 0

for i in range(n//2+1):
    for j in range( (n-1)//2-i, (n-1)//2+i+1):
        count += l[i][j]
        if(i != (n-1)//2):
            count += l[n-i-1][j]
        if j == n-1:
            break
print(count)