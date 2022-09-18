import sys
#sys.stdin=open("input.txt","rt")

def digit_sum(x):
    hap = 0
    while x!= 0:
        hap += x % 10
        x = x // 10
    return hap

n = int(input())
nList = list(map(int, input().split()))

max, answer = 0, 0

for i in range(n):
    now = digit_sum(nList[i])
    if(max < now):
        max = now
        answer = i

print(nList[answer])