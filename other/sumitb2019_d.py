n = int(input())
s = input()

ans = 0
# 000 ～　999 がsから作成できるか確認していく
for i in range(1000):
    p = str(i).zfill(3)

    s_index_100 = s.find(p[2])
    if s_index_100 == -1:
        continue

    s_index_10 = s.find(p[1], s_index_100+1)
    if s_index_10 == -1:
        continue

    s_index_1 = s.find(p[0], s_index_10+1)
    if s_index_1 == -1:
        continue
    ans += 1

print(ans)