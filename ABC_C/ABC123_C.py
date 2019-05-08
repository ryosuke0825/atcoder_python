S = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

min_traffic = min(A, B, C, D, E)
print((-(-S // min_traffic))+4)

# city = [S, 0, 0, 0, 0, 0]
# ans = 0
# while city[5] != S:
#     tmp = city[:]

#     if tmp[0] >= A:
#         city[0] = tmp[0] - A
#         city[1] += A
#     elif tmp[0] != 0:
#         city[1] += tmp[0]
#         city[0] -= tmp[0]

#     if tmp[1] >= B:
#         city[1] = city[1] - B
#         city[2] += B
#     elif tmp[1] != 0:
#         city[2] += tmp[1]
#         city[1] -= tmp[1]

#     if tmp[2] >= C:
#         city[2] = city[2] - C
#         city[3] += C
#     elif tmp[2] != 0:
#         city[3] += tmp[2]
#         city[2] -= tmp[2]

#     if tmp[3] >= D:
#         city[3] = city[3] - D
#         city[4] += D
#     elif tmp[3] != 0:
#         city[4] += tmp[3]
#         city[3] -= tmp[3]

#     if tmp[4] >= E:
#         city[4] = city[4] - E
#         city[5] += E
#     elif tmp[4] != 0:
#         city[5] += tmp[4]
#         city[4] -= tmp[4]

#     ans += 1
#     print(ans)

# print(ans)
