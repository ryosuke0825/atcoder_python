l1, l2, l3 = map(int, input().split())

if l1 != l2 and l1 != l3:
    print(l1)
elif l2 != l1 and l2 != l3:
    print(l2)
else:
    print(l3)
