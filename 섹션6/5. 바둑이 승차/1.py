import sys
#sys.stdin=open("input.txt", "r")

def DFS(v,sum):
    if sum>c:
        return
    if v==n:
        global m
        if sum>m and sum<=c:
            m=sum
    else:
        DFS(v+1,sum+dogs[v])
        DFS(v+1,sum)

if __name__=="__main__":
    c,n=map(int,input().split())
    dogs=[int(input()) for _ in range(n)]
    m=0
    DFS(0,0)
    print(m)