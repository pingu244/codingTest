import sys
#sys.stdin=open("input.txt","rt")

n=input()
n=list(map(str,n))
stack=[]

for i in n:
    if i.isdecimal():
        stack.append(int(i))
    else:
        b=stack.pop()
        a=stack.pop()
        if i=='+':
            a=a+b
        elif i=='-':
            a=a-b
        elif i=='*':
            a=a*b
        elif i=='/':
            a=a/b
        stack.append(a)

print(stack[0])