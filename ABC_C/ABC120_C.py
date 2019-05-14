# S = input()
# ans = 0
# while True:
#     if S.count("01") == 0 and S.count("10") == 0:
#         break

#     if S.count("01") > 0:
#         ans += S.count("01")*2
#         S = S.replace("01", "")

#     if S.count("10") > 0:
#         ans += S.count("10")*2
#         S = S.replace("10", "")

# print(ans)

S = input()
print(min(S.count("0"),S.count("1"))*2)
