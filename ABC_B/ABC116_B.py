s = int(input())

a = []
a.append(s)

i = 0
while True:
    if a[i] % 2 == 0:
        tmp = a[i]/2
    else:
        tmp = a[i]*3+1

    if tmp in a:
        print(i+2)
        break
    else:
        a.append(tmp)
        i += 1
