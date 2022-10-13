import sys
import heapq as hp
#sys.stdin = open("input.txt", 'r')

a=[]
while True:
    n=int(input())
    if n==-1:
        break
    elif n==0:
        if len(a)==0:
            print(-1)
        else:
            print(-hp.heappop(a))
    else:
        hp.heappush(a,-n)