import sys
import math
#sys.stdin=open("input.txt","rt")

def reverse(x):
    num = list(str(x))
    num.reverse()
    answer = 0
    length = len(num)
    for i in range(length):
        answer += int(num[i]) * pow(10, length-i-1)
    return answer

def isPrime(x):
    if(x==1):
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i == 0):
            return False
    return True
    
n = int(input())
nList = list(map(int, input().split()))
answer = []

for i in range(n):
    value = reverse(nList[i])
    if isPrime(value):
        answer.append(value)


print(*answer, end=' ')