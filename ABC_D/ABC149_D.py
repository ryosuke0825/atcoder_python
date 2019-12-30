N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

# 勝てる手の組み合わせを持つ辞書型を生成する
win_hand = {"r": "p", "s": "r", "p": "s"}
ANS = []

# 勝てる手の配列を作成する
for i in range(N):
    ANS.append(win_hand[T[i]])

# 配列を１つの文字列にする
ans = "".join(ANS)

# 制約のある手以降を探索
for i in range(K, N):
    # K回前の手と同じなら出した手をxに置換する
    if ans[i] == ans[i-K]:
        ans = ans[:i] + "x" + ans[i+1:]

# 各手の数と得られる点数を求める
point = ans.count("r")*R + ans.count("s")*S + ans.count("p")*P

print(point)
