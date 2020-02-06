n = int(input())
d, x = map(int, input().split())

# 各参加者がチョコレートを食べる日付を取得してリストへ格納する
al = [0 for _ in range(n)]
for i in range(n):
    al[i] = int(input())

ans = 0
for i in al:
    ans += ((d-1)//i)
    ans += 1

print(ans+x)
