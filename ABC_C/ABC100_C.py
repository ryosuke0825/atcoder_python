n = int(input())
a = list(map(int, input().split()))

al = []
for at in a:
    bin_str = bin(at)
    if bin_str.rfind('0')+1 == len(bin_str):
        al.append(bin_str.rfind('0')-bin_str.rfind('1'))
    else:
        al.append(0)

print(sum(al))
