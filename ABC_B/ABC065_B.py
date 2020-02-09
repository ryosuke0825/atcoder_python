n = int(input())
buttons = [0 for _ in range(n)]
for i in range(n):
    buttons[i] = int(input())

light = buttons[0]
for i in range(n):
    if light == 2:
        print(i+1)
        break
    light = buttons[light-1]
else:
    print(-1)
