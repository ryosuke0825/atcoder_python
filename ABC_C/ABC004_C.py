N = int(input())
zumi = ['123456']
zumi_hash = {}
zumi_hash['123456'] = True

card = ['1', '2', '3', '4', '5', '6']

for i in range(N):
    irekae_1 = (i % 5)+1
    irekae_2 = (i % 5)+2

    card[irekae_1-1], card[irekae_2-1] = card[irekae_2-1], card[irekae_1-1]
    tmp_ans = ''.join(card)
    if tmp_ans in zumi_hash:
        break

    zumi_hash[tmp_ans] = True
    zumi.append(tmp_ans)

else:
    print(''.join(card))
    exit(0)

print(zumi[N % len(zumi)])
