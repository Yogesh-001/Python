t=int(input())
for _ in range(t):
    N,x,k=map(int,input().split())
    if x%k==0:
        print("YES")
    elif ((N+1)-x)%k==0:
        print("YES")
    else:
        print("NO")
