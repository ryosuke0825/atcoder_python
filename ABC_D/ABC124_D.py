from itertools import accumulate


def main():
    n, k = map(int, input().split())
    s = input()

    # 配列を下記で変換
    # '11000' = [2, 3, 0]
    # '011000' = [0, 1, 2, 3, 0]
    # '1'の長さで始まり、'1'の長さで終わるようにする

    # 0と1の境目にカンマを挿入する
    s = s.replace('01', '0,1')
    s = s.replace('10', '1,0')

    # 0と1の長さを求めてリストに格納する
    len_list = []
    for string in s.split(','):
        len_list.append(len(string))

    # '1'の長さで始まり、'1'の長さで終わるようにする
    # 最初が0の時は、リスト「len_list」の最初に0を追加
    # 最後が0の時は、リスト「len_list」の最後に0を追加
    if s[0] == '0':
        len_list = [0] + len_list
    if s[-1] == '0':
        len_list = len_list + [0]

    # 文字列のすべてを1にできる場合は、文字列の長さを出力する
    if 2 * k + 1 >= len(len_list):
        print(n)
        return

    # すべてを1にできない場合、最大の長さを求める
    # リストの最初から順番に足した時のリストを「accumulate」で求める
    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    sum_list = [0] + list(accumulate(len_list))
    max_len = 0

    # リストの先頭からリストの大きさ-「(2 * k + 1) + 1」まで偶数（1の長さの部分）でループ
    # リストの大きさ-「(2 * k + 1) + 1」は、全て1にできる部分のため、以降は不要となる。
    for i in range(0, len(len_list) - (2 * k + 1) + 1, 2):
        # 「i + (2 * k + 1)」は現在の位置から全て1にできる位置
        handstand_len = sum_list[i + (2 * k + 1)] - sum_list[i]
        if max_len < handstand_len:
            max_len = handstand_len
    print(max_len)


if __name__ == '__main__':
    main()
