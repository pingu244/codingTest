import sys
import re
#sys.stdin=open("input.txt","rt")
    
n = input()
temp = []
count = 1

num = re.findall(r'\d+', n)
num = int("".join(num))

for i in range(2, num+1):
    if num % i == 0:
        count += 1

print(num,count,sep='\n')