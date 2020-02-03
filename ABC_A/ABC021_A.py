n = int(input())
ret_list = []

if n % 2 == 1:
    n -= 1
    ret_list.append(1)

for _ in range(n//2):
    ret_list.append(2)

print(len(ret_list))
for i in ret_list:
    print(i)
