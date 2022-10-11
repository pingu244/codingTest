import sys
#sys.stdin = open("input.txt", 'r')

n=int(input())
list=[]

for _  in range(n):
    list.append(input())

for _ in range(n-1):
    word=input()
    if word in list:
        list.pop(list.index(word))
print(*list)