import sys
#sys.stdin=open("input.txt", "r")

n,k=map(int,input().split())
count = 0

for i in range (n):
    if n%(i+1)==0:
        count+=1
    if count == k:
        print(i+1)
        break
else:
    print(-1)