def uruu_calculation(y):
    return y//4 - y//100 + y//400


A, B = map(int, input().split())
print(uruu_calculation(B)-uruu_calculation(A-1))
