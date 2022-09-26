import sys
#sys.stdin=open("input.txt","rt")

num, k= map(int, input().split())
n=list(map(int,str(num)))   #num을 리스트화
i=0 # i번째 수 뺄지말지 확인

while k>0:
    # m은 max
    m=i

    # 끝까지 돌았는데도 딱히 할 거가 없을때(지금이 가장 큰 수)
    if len(n)-k==i:
        for _ in range(k):
            n.pop()
        break

    # i부터 k번째 안에 i번째보다 큰 수 찾기
    for j in range(i+1,i+k+1):
        if n[m]<n[j]:
            m=j
    if m>i:
        for _ in range(m-i):    # 거기까지 pop
            n.pop(i)
            k-=1
    i+=1

for i in n:
    print(i,end='')