n=int(input())

for i in range(n):
    n-=1
    y=n
    for a in range(y+2):
        print(a, end=' ')
        y-=1
    print()