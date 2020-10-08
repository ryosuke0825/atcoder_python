S = input()

# 文字列の先頭と末尾に注目する。
# １、先頭と末尾が同じ文字なら両方消す
# ２、先頭と末尾のどちらかがxならxを消してカウントアップ
# ３、先頭と末尾が異なりxでもないなら消せない（-1）
ans = 0
l = 0
r = len(S)-1
while l < r:
    if S[l] == S[r]:
        l += 1
        r -= 1
    elif S[l] == 'x':
        l += 1
        ans += 1
    elif S[r] == 'x':
        r -= 1
        ans += 1
    else:
        ans = -1
        break
print(ans)
