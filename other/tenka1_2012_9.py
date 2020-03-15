import math


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


n = int(input())
ans = 0
for i in range(1, n):
    if is_prime(i):
        ans += 1
print(ans)
