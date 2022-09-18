import sys
#sys.stdin=open("input.txt","rt")

n=int(input())
l = [list(map(int, input().split())) for _ in range(n)]
count = 0

for i in l:
    for j in l:
        if i==j:
            continue
        if i[0]<j[0] and i[1]<j[1]:
            break
    else:
        count+=1

print(count)