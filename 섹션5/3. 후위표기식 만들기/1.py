import sys
#sys.stdin = open("input.txt", 'r')

n=input()
stack=[]
answer=''

for i in n:
    if i.isdecimal():
        answer+=i

    elif i=='*' or i=='/':
        while stack:
            a=stack.pop()
            if a=='*' or a=='/':
                answer+=a
            else:
                stack.append(a)
                break
        stack.append(i)
    elif i=='+' or i=='-':
        while stack:
            a=stack.pop()
            if a=='(':
                stack.append(a)
                break
            else:
                answer+=a
        stack.append(i)
    elif i==')':
        while stack:
            a=stack.pop()
            if a=='(':
                break
            else:
                answer+=a
    else:
        stack.append(i)

while stack:
    answer+=stack.pop()
print(answer)