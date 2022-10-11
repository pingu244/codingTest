import sys
#sys.stdin = open("input.txt", 'r')

lesson = input()
n=int(input())

for p in range(n):
    list=input()
    it = 0
    for a in range(len(list)):
        if it==len(lesson):
            print('#%d YES' %(p+1))
            break
        if list[a]==lesson[it]:
            it+=1
            continue
    else:
        if it==len(lesson):
            print('#%d YES' %(p+1))
        else:
            print('#%d NO' %(p+1))
    