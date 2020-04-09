A, B = input().split()

ans = []
ans.append(int(A)-int(B))

a = '9'+A[1:]
ans.append(int(a)-int(B))

a = '1'+A[1:]
ans.append(int(a)-int(B))

a = A[0] + '9' + A[2]
ans.append(int(a)-int(B))

a = A[0] + '0' + A[2]
ans.append(int(a)-int(B))

a = A[:2]+'9'
ans.append(int(a)-int(B))

a = A[:2]+'0'
ans.append(int(a)-int(B))

b = '9'+B[1:]
ans.append(int(A)-int(b))

b = '1'+B[1:]
ans.append(int(A)-int(b))

b = B[0] + '9' + B[2]
ans.append(int(A)-int(b))

b = B[0] + '0' + B[2]
ans.append(int(A)-int(b))

b = B[:2]+'9'
ans.append(int(A)-int(b))

b = B[:2]+'0'
ans.append(int(A)-int(b))

print(max(ans))
