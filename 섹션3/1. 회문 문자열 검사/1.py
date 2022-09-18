import sys
#sys.stdin=open("input.txt","rt")
    
n = int(input())

for i in range(n):
    word = str(input())
    word = word.lower()
    temp = word[::-1]
    print('#%d ' %(i+1), end=' ')
    if word == temp:
        print('YES')
    else:
        print('NO')