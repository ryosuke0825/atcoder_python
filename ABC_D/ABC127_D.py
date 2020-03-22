n, m = map(int, input().split())
A = list(map(int, input().split()))

CB = []
for _ in range(m):
    b, c = map(int, input().split())
    CB.append([c, b])

CB.sort(reverse=True)
A.sort()
index = 0
for i in range(m):
    if index >= n:
        break
    elif A[index] >= CB[i][0]:
        break

    for j in range(CB[i][1]):
        if index >= n:
            break
        elif A[index] >= CB[i][0]:
            break

        A[index] = CB[i][0]
        index += 1

print(sum(A))
