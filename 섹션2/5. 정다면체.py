import sys
#sys.stdin=open("input.txt","rt")

n, m = map(int, input().split())

for i in range(n+1, m+2):
    print(i,  end=' ')
