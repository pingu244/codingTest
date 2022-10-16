import sys
from collections import deque
#sys.stdin = open("input.txt", 'r')

n=list(input())
k=int(input())

for i in range(1,k+1):
    word=deque(input())
    a=0
    while word:
        if a<len(n):
            if word.popleft()==n[a]:
                a+=1
        else:
            print('#%d YES' %i)
            break
    else:
        if a==len(n):
            print('#%d YES' %i)
        else:
            print('#%d NO' %i)


