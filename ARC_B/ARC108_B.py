N = int(input())
S = input()

x = ''
for i in range(N):
    x += S[i]
    if x.endswith('fox'):
        x = x[:len(x)-3]
print(len(x))
