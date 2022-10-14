import sys
#sys.stdin = open("input.txt", 'r')

n=int(input())
list=[tuple(map(int,input().split())) for _ in range(n)]
list.sort(key=lambda x:x[1])
cnt=1
a=0
for i in range(1,n):
    if list[a][1]<=list[i][0]:
        cnt+=1
        a=i
 
print(cnt)