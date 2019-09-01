import math

for n in range(51):
    m = 2 ** n - 1
    for j in range(2, int(math.sqrt(m)) + 1):
        if m % j == 0:
            break
    else:
        print(m)
