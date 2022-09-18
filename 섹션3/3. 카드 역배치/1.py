import sys
#sys.stdin=open("input.txt","rt")

num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
l = [list(map(int, input().split())) for _ in range(10)]

for i in l:
    for  j in range((i[1] - i[0] +1)//2):
        n = i[0] -1 + j
        m = i[1] -1 - j
        t = num[n]
        num[n] = num[m]
        num[m] = t

print(*num)