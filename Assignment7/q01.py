rows = 5
for i in range(1, rows+1):
    print(" " * (rows - i) + "* " * i)
for i in range(rows-1, 0, -1):
    print(" " * (rows - i) + "* " * i)
