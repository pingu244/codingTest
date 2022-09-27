import sys
#sys.stdin=open("input.txt","rt")

n,k=map(int,input().split())
prince=[a for a in range(n+1)]
prince.pop(0)
# i번째 pop
i=0

while len(prince)>1:
    i += k-1    # 0부터 시작이니 -1
    # i가 길이보다 크면 나머지계산
    if len(prince)<=i:
        i=i%(len(prince))
    prince.pop(i)

print(prince[0])