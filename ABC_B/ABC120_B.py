import fractions

a, b, k = map(int, input().split())
gcd = fractions.gcd(a, b)
divisor_list = []

if gcd == 1:
    divisor_list = [1]
else:
    divisor_list.append(1)
    for i in range(2, gcd // 2 + 1):
        if gcd % i == 0:
            divisor_list.append(i)
    divisor_list.append(gcd)

print(divisor_list[len(divisor_list)-1-k+1])
