import sys
#sys.stdin=open("input.txt","rt")

l = [list(map(int, input().split())) for i in range(9)]

# 1-9까지 다 있나 확인하는 함수
def check(list):
    a = 1
    for i in list:
        a *= i
    if a==1:
        return True
    else:
        return False

# 행 검사
for i in l:
    test = [0] * 10
    for j in i:
        test[j] = 1
    test.pop(0)
    if not check(test):
        print('NO')
        exit()

# 열 검사
for col in range(9):
    test = [0] * 10
    for row in range(9):
        test[l[row][col]] = 1
    test.pop(0)
    if not check(test):
        print('NO')
        exit()

# 사각형 검사
for i in range(3):
    for j in range(3):
        test = [0] * 10
        for row in range(i*3, (i+1)*3):
            for col in range(j*3, (j+1)*3):
                test[l[row][col]] = 1
        test.pop(0)
        if not check(test):
            print('NO')
            exit()

print('YES')