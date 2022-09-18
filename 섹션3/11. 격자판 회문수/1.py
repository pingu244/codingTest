import sys
#sys.stdin=open("input.txt","rt")

l = [list(map(int, input().split())) for i in range(7)]
cnt = 0

# 가로
for i in l:
    temp = []
    for j in i:
        
        if len(temp)<5:
            temp.append(j)
        else:
            temp.pop(0)
            temp.append(j)
        if len(temp)==5:
            if temp[0] == temp[4] and temp[1]==temp[3]:
                    cnt += 1
            

# 세로
for j in range(7):
    temp = []
    for i in range(7):
        if len(temp)<5:
            temp.append(l[i][j])
        else:
            temp.pop(0)
            temp.append(l[i][j])
        if len(temp)==5:
            if temp[0] == temp[4] and temp[1]==temp[3]:
                    cnt += 1

print(cnt)
