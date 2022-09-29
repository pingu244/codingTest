import sys
#sys.stdin=open("input.txt","rt")

n,m = map(int, input().split())
l = list(map(int, input().split()))
count = 0

for i in range(n):
    value = 0
    for j in range(i, n):
        if j==0 and l[j]>m:
            break
        value += l[j]
        if value == m:
            count += 1
            break
        elif value > m:
            break
print(count)