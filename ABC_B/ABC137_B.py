k, x = map(int, input().split())
ans_list = range(x-k+1, x+k)

# アンパック。リストを分割して渡す。
print(*ans_list)
