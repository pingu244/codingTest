import sys
#sys.stdin=open("input.txt","rt")

n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
maxV = -1
cross = [0,0]

for i in range(n):
    rowSum = 0
    colSum = 0
    for j in range(n):
        rowSum += l[i][j]
        colSum += l[j][i]
    maxV = max(maxV, rowSum, colSum)
    cross[0] +=l[i][i]
    cross[1] += l[i][n-i-1]
print(max(cross[0],cross[1],maxV))