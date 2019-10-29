W, H, x, y = map(int, input().split())

menseki = W*H
mensekix = min(x, W-x) * H
mensekiy = W * min(y, H-y)
ans1 = min(mensekix, mensekiy)
ans2 = 0 if mensekix == mensekiy else 1
print('%f %d' % (ans1, ans2))
