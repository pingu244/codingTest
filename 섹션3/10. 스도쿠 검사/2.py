import sys
#sys.stdin = open("input.txt", 'r')
m=[list(map(int, input().split())) for _ in range(9)]

for i in range(9):
    col=[1]*10
    row=[1]*10
    for j in range(9):
        col[m[i][j]]-=1
        row[m[j][i]]-=1
    col.pop(0)
    row.pop(0)
    if max(col) != 0 or max(row)!=0:
        print('NO')
        break

    box=[1]*10
    for a in range(3):
        r=a+i//3*3
        for b in range(3):
            c=b+i%3*3
            box[m[r][c]]-=1
    box.pop(0)
    if max(box)!=0:
        print('NO')
        break
else:
    print('YES')