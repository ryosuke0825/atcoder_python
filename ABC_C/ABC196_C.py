N = int(input())
L = len(str(N))

ans = 0
for i in range(2, L+1, 2):
    if i == L:
        head = int(str(N)[:i//2])
        tail = int(str(N)[i//2:])
        if head <= 9:
            if head > tail:
                head -= 1
            ans += head
        else:
            if head > tail:
                head -= 1
            ans += max(0, head-ans)
    else:
        ans += 9*int('1'+'0'*((i//2)-1))
print(ans)
