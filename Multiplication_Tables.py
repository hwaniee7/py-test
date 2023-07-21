
for i in range(2, 10):
    for j in range(1,10):
        print(i, "*", j, "=", j * j)


for i in range(2, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == 4 and j == 9:
                continue
            print(i, "*", j, "*", k, "=", j * j * k)
