N = int(input())
W = input()

hs = {'b': '1', 'c': '1', 'd': '2', 'w': '2', 't': '3', 'j': '3', 'f': '4', 'q': '4', 'l': '5', 'v': '5',
      's': '6', 'x': '6', 'p': '7', 'm': '7', 'h': '8', 'k': '8', 'n': '9', 'g': '9', 'z': '0', 'r': '0', }

ans = ''
for i in range(len(W)):
    if W[i].lower() in hs:
        ans = ans+hs[W[i].lower()]
    elif W[i] == ' ' and len(ans) != 0 and ans[-1] != ' ':
        ans += W[i]

print(ans.strip())
