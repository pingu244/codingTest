import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

subject=input()
n=int(input())
for i in range(1,n+1):
    word=input()
    subQ=deque(subject)
    for x in word:
        if x in subQ:
            if x!=subQ.popleft():
                print('#%d NO' %i)
                break
    else:
        if len(subQ)==0:
            print('#%d YES' %i)
        else:
            print('#%d NO' %i)