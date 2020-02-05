n = int(input())
al = list(map(int, input().split()))

reverse_list = []
for a in al:
    reverse_list.append(1/a)

print(1/sum(reverse_list))
