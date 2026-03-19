import math
n, t = map(int, input().split())
books = list(map(int, input().split()))

sumi = 0
i = 0
max_val = 0
for j in range(n):
    sumi += books[j]

    while i <= j and sumi > t:
        sumi -= books[i]
        i += 1

    # print(i, j)
    # print(sumi, t)
    max_val = max(j - i + 1, max_val)
print(max_val)