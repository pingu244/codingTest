import sys
#sys.stdin=open("input.txt", "r")

card = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for _ in range(10):
    a,b = map(int,input().split())
    temp = card[a:b+1]
    temp.reverse()
    answer=[]
    answer.extend(card[:a])
    answer.extend(temp)
    answer.extend(card[b+1:])
    card = answer
card.remove(0)
print(*card)