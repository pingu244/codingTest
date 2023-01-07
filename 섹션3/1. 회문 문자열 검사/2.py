import sys
#sys.stdin=open("input.txt", "r")

n=int(input())

for i in range (n):
    word = input()
    word = word.lower()
    l = len(word)
    for a in range(l//2):
        if word[a] != word[l-1-a]:
            print("#%d NO" % (i+1))
            break
    else:
        print("#%d YES" % (i+1))