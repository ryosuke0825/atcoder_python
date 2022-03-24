N = int(input())

one_name, one_h = input().split()
two_name, two_h = input().split()

if int(two_h) > int(one_h):
    one_name, two_name = two_name, one_name
    one_h, two_h = two_h, one_h

for _ in range(N-2):
    s, t = input().split()

    if int(t) > int(one_h):
        one_name, two_name = s, one_name
        one_h, two_h = t, one_h
    elif int(t) > int(two_h):
        two_name = s
        two_h = t

print(two_name)
