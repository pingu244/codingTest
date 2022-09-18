import sys
#sys.stdin=open("input.txt","rt")

t = int(input())

for i in range(t):
  n,s,e,k = map(int, input().split())
  nList = list(map(int, input().split()))

  slice = nList[s-1:e]

  slice.sort()
  
  print ("#%d %d" %(i+1, slice[k-1]))