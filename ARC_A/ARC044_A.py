import math


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def digitSum(n):
    s = str(n)
    array = list(map(int, s))
    return sum(array)


n = int(input())
if n == 1:
    print('Not Prime')
    exit(0)
if is_prime(n):
    print('Prime')
else:
    if int(str(n)[-1]) % 2 != 0 and int(str(n)[-1]) != 5 and digitSum(n) % 3 != 0:
        print('Prime')
    else:
        print('Not Prime')
