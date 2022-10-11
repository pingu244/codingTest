import sys
#sys.stdin = open("input.txt", 'r')

n=list(map(str,input()))
m=input()

for i in range(len(n)):
    if m[i] in n:
        n.pop(n.index(m[i]))
    else:
        print('NO')
        break
else:
    if not n:
        print('YES')