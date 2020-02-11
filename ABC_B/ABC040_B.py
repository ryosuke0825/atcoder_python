n = int(input())

h = 1
w = 1
for i in range(1, n+1):
    for j in range(1, n+1):
        if i*j > n:
            if (n-h*w+abs(h-w) > n-i*(j-1)+abs(i-(j-1))):
                h = i
                w = j-1
            break

print(n-h*w+abs(h-w))
