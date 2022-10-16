import sys
#sys.stdin = open("input.txt", 'r')

n,k=map(int, input().split())
l=list(map(int, input().split()))
answer=[]

for i in range(n-2):
    for j in range(i+1,n-1):
        for p in range(j+1, n):
            answer.append(l[i]+l[j]+l[p])

answer=sorted(list(set(answer)),reverse=True)
print(answer[k-1])

