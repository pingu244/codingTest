import sys
#sys.stdin=open("input.txt","rt")

num, k= map(int, input().split())
n=list(map(int,str(num)))   #num을 리스트화
answer=[]

i=0 # n의 iterator변수
while k>0 and i<len(n):
    if not answer:
        answer.append(n[i])
        i +=1
    elif n[i]>answer[-1]:
        answer.pop()
        k-=1
    else:
        answer.append(n[i])
        i +=1
answer += n[i:]

if k>0:
    for _ in range(k):
        answer.pop()

for i in answer:
    print(i,end='')