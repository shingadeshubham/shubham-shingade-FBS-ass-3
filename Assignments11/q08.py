n = 10
for i in range(n, 0, -1):
    row = []
    for j in range((i-1)*n+1, i*n+1):
        row.append(j)
    if i % 2 == 0:
        row.reverse()
    print(row)
