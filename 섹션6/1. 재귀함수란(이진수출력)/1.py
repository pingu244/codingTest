import sys
#sys.stdin = open("input.txt", 'r')

def recursion(n):
    if n>=2:
        recursion(n//2)
        print(n%2, end='')
    elif n==1:
        print(1, end='')

n=int(input())
recursion(n)