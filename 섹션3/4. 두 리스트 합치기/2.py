import sys
#sys.stdin=open("input.txt", "r")

answer=[]
n = int(input())
answer = list(map(int,input().split()))
m = int(input())
answer.extend(list(map(int,input().split())))

answer.sort()
print(*answer)