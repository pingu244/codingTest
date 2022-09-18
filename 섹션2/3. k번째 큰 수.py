import sys
#sys.stdin=open("input.txt","rt")

n,k = map(int, input().split())
nList = list(map(int, input().split()))
plusList = []

for i in range(n):
    for j in range(i+1, n):
        for p in range(j+1, n):
            plusList.append(nList[i]+nList[j]+nList[p])

plusList = list(set(plusList))  # 중복 제거
plusList.sort(reverse=True) # 내림차순

print(plusList[k-1])