import sys
#sys.stdin=open("input.txt", "r")

n=list(input())
n.reverse()
count = 1
num = 0

for i in n:
    if i.isdecimal():
        num += int(i)*count
        count *= 10
print(num)

count = 0
for j in range(1,num+1):
    if num % j == 0:
        count+=1
print(count)