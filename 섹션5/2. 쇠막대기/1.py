import sys
#sys.stdin=open("input.txt","rt")

l=input()
n=[]
answer = 0

# ( -> 1, ) -> 2, () -> 0 으로 바꾸는 과정
for i in range(len(l)):
    if l[i]=='(':
        n.append(1)
    else:
        if n[-1]==1:
            n.pop()
            n.append(0)
        else:
            n.append(2)

# stick 스택과 laser스택을 따로 생성
stick=[]
laser=[]
for i in range(len(n)):
    if n[i]==0:
        laser.append(i)
    elif n[i]==1:
        stick.append(i)
    else:   # 꺼내야할때면
        num=stick.pop()
        cnt=0
        # 꺼낼 번째 보다 큰 번째들(=막대기 시작 이후에 있는 레이저들)만 더함
        for j in laser:
            if j>num:
                cnt +=1 # 레이저로 나누면 레이저수+1
        answer += cnt+1

print(answer)