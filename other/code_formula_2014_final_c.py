S = input()

ans = 0
users = {}
flag = False
user_name = ''
for i in range(len(S)):
    if flag:
        if S[i] != '@' and S[i] != ' ':
            user_name += S[i]
        else:
            flag = False
            if len(user_name) >= 1:
                if not(user_name in users):
                    users[user_name] = user_name
            user_name = ''

            if S[i] == '@':
                flag = True
    else:
        if S[i] == '@':
            flag = True
if user_name != '':
    if not(user_name in users):
        users[user_name] = user_name

for k, v in sorted(users.items(), key=lambda x: x[1]):
    print(v)
