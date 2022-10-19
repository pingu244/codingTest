import sys
sys.stdin=open("input.txt", "r")

def DFS(v,cnt):
    if cnt==m:
        for i in range(len(ch)):
            if ch[i]==1:
                print(i, end=' ')
                ch[-1]+=1
        print()
    else:
        ch[v+1]=1
        DFS(v+1,cnt+1)
        ch[v+1]=0
        DFS(v+1,cnt)

if __name__=="__main__":
    n,m=map(int,input().split())
    ch=[0]*(n+2)
    DFS(0,0)
    print(ch[-1])