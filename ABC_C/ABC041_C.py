N = int(input())
A = list(map(int, input().split()))

students = []
for i in range(N):
    students.append([A[i], i+1])

students.sort(reverse=True)
for i in range(N):
    print(students[i][1])
