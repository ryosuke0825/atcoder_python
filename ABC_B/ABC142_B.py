n, k = map(int, input().split())
h_list = list(map(int, input().split()))


ans_list = [h for h in h_list if h >= k]
ans = len(ans_list)

print(ans)
