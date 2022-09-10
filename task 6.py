n=int(input())
for i in range(1, n+1):
    for a in range(i, 0, -1):
        print(a, end=' ')
    print()