import sys
#sys.stdin=open("input.txt","rt")

n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
col, cnt = 0,0

for row in range(n):
    for col in range(n):
        answer = [0,0,0,0]
        if row != 0:
            if l[row][col] > l[row-1][col]:
                answer[0] = 1
        else:
            answer[0] = 1

        if row != n-1:
            if l[row][col] > l[row+1][col]:
                answer[1] = 1
        else:
            answer[1] = 1

        if col != 0:
            if l[row][col] > l[row][col-1]:
                answer[2] = 1
        else:
            answer[2] = 1

        if col != n-1:
            if l[row][col] > l[row][col+1]:
                answer[3] = 1
        else:
            answer[3] = 1

        if sum(answer)==4:
            cnt += 1
            col += 1

print(cnt)