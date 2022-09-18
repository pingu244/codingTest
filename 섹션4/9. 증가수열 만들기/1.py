import sys
#sys.stdin=open("input.txt","rt")

n=int(input())
l = list(map(int, input().split()))
answer=[]
aList=[]

if l[0]<l[-1]:
    aList.append(l.pop(0))
    answer.append('L')
else:
    aList.append(l.pop(-1))
    answer.append('R')

while len(l)>0:
    if aList[-1]<l[0]:
        if aList[-1]<l[-1]:
            if l[0]>l[-1]:
                aList.append(l.pop(-1))
                answer.append('R')
            else:
                aList.append(l.pop(0))
                answer.append('L')
        else:
            aList.append(l.pop(0))
            answer.append('L')
    elif aList[-1]<l[-1]:
        aList.append(l.pop(-1))
        answer.append('R')
    else:
        break

print(len(aList))
for i in answer:
    print(i,end='')