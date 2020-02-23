h, w = map(int, input().split())
for i in range(1, h+1):
    s = input().split()
    if 'snuke' in s:
        print(chr(65+s.index('snuke'))+str(i))
